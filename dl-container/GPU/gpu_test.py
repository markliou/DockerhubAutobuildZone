#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import jax
import jax.numpy as jnp
import torch


def check_tf():
    assert (len(tf.config.list_physical_devices('GPU')) > 0)


def check_jax():
    assert (jax.devices()[0].platform != 'cpu')


def check_torch():
    assert (torch.cuda.is_available())

def check_gpu_counting_function():
    sample = np.array([.1, .2, .3])

    # test tensorflow
    tfV = tf.Variable(sample)
    assert(((tfV * 2).numpy() == sample * 2).all())

    # test jax
    jnpV = jnp.array(sample)
    assert((np.array(jnpV * 2) == (sample * 2).astype(np.float32)).all())

    # test pytorch
    torchV = torch.FloatTensor(sample)
    assert((np.array((torchV * 2)) == (sample * 2).astype(np.float32)).all())

def main():
    check_tf()
    check_jax()
    check_torch()
    check_gpu_counting_function()


if __name__ == "__main__":
    main()
