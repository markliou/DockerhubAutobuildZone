#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import jax
import jaxlib
import jax.numpy as jnp
import torch


def print_env_info():
    print("Checking GPU test environment...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"PyTorch CUDA version: {torch.version.cuda}")
    print(f"PyTorch cuDNN version: {torch.backends.cudnn.version()}")
    print(f"JAX version: {jax.__version__}")
    print(f"jaxlib version: {jaxlib.__version__}")
    print(f"JAX default backend: {jax.default_backend()}")
    print(f"JAX devices: {jax.devices()}")


def check_jax():
    print("Checking jax gpu available...")
    gpu_devices = [
        device for device in jax.devices() if device.platform in ("gpu", "cuda")
    ]
    assert gpu_devices, f"No JAX GPU device found: {jax.devices()}"
    device = gpu_devices[0]
    print(f"Using JAX device: {device}")

    print("Checking JAX GPU tensor function...")
    sample = np.array([.1, .2, .3], dtype=np.float32)
    jax_tensor = jax.device_put(jnp.asarray(sample), device)
    doubled = (jax_tensor * 2).block_until_ready()
    np.testing.assert_allclose(np.asarray(doubled), sample * 2, rtol=1e-6, atol=1e-6)

    print("Checking JAX jit matmul on GPU...")
    matrix = (np.arange(1024, dtype=np.float32).reshape(32, 32) / 1024.0)
    identity = np.eye(32, dtype=np.float32) * 2.0

    @jax.jit
    def jit_matmul(x, y):
        return (x @ y) + jnp.float32(1.0)

    jax_matrix = jax.device_put(jnp.asarray(matrix), device)
    jax_identity = jax.device_put(jnp.asarray(identity), device)
    result = jit_matmul(jax_matrix, jax_identity).block_until_ready()
    np.testing.assert_allclose(
        np.asarray(result),
        (matrix @ identity) + 1.0,
        rtol=1e-5,
        atol=1e-5,
    )


def check_torch():
    print("Checking torch gpu available...")
    assert torch.cuda.is_available(), "No PyTorch CUDA device found"
    assert torch.cuda.device_count() > 0, "PyTorch reports zero CUDA devices"
    device = torch.device("cuda:0")
    print(f"Using PyTorch device: {torch.cuda.get_device_name(device)}")
    print(f"PyTorch device capability: {torch.cuda.get_device_capability(device)}")

    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False

    print("Checking PyTorch GPU tensor function...")
    sample = np.array([.1, .2, .3], dtype=np.float32)
    torch_tensor = torch.tensor(sample, dtype=torch.float32, device=device)
    assert torch_tensor.is_cuda, "PyTorch tensor is not on CUDA"
    doubled = torch_tensor * 2
    torch.cuda.synchronize(device)
    np.testing.assert_allclose(
        doubled.detach().cpu().numpy(),
        sample * 2,
        rtol=1e-6,
        atol=1e-6,
    )

    print("Checking PyTorch matmul on GPU...")
    matrix = torch.arange(1024, dtype=torch.float32, device=device).reshape(32, 32)
    matrix = matrix / 1024.0
    identity = torch.eye(32, dtype=torch.float32, device=device) * 2.0
    result = (matrix @ identity) + 1.0
    assert result.is_cuda, "PyTorch matmul result is not on CUDA"
    torch.cuda.synchronize(device)
    expected = (
        (np.arange(1024, dtype=np.float32).reshape(32, 32) / 1024.0)
        @ (np.eye(32, dtype=np.float32) * 2.0)
    ) + 1.0
    np.testing.assert_allclose(
        result.detach().cpu().numpy(),
        expected,
        rtol=1e-5,
        atol=1e-5,
    )


def check_tf():
    print("Checking tensorflow gpu available...")
    import tensorflow as tf

    assert len(tf.config.list_physical_devices("GPU")) > 0

    sample = np.array([.1, .2, .3], dtype=np.float32)
    print("Checking tensorflow function ...")
    tf_tensor = tf.Variable(sample)
    np.testing.assert_allclose((tf_tensor * 2).numpy(), sample * 2)



def main():
    print_env_info()
    # check_tf()
    check_torch()
    check_jax()
    print("GPU smoke test passed.")

if __name__ == "__main__":
    main()
