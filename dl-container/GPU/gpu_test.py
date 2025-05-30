#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import jax
import jax.numpy as jnp
import torch


def check_tf():
    print("Checking tensorflow gpu available...")
    assert (len(tf.config.list_physical_devices('GPU')) > 0)

    # test tensorflow
    sample = np.array([.1, .2, .3])
    print("Checking tensorflow function ...")
    tfV = tf.Variable(sample)
    assert(((tfV * 2).numpy() == sample * 2).all())


def check_jax():
    print("Checking jax gpu available...")
    assert (jax.devices()[0].platform != 'cpu')

    # test jax
    sample = np.array([.1, .2, .3])
    print("Checking jax function ...")
    jnpV = jnp.array(sample)
    assert((np.array(jnpV * 2) == (sample * 2).astype(np.float32)).all())


def check_torch():
    print("Checking torch gpu available...")
    assert (torch.cuda.is_available())

    # test pytorch
    sample = np.array([.1, .2, .3])
    print("Checking torch function ...")
    torchV = torch.FloatTensor(sample)
    assert(((torchV * 2).numpy() == (sample * 2).astype(np.float32)).all())



def main():
    check_tf()
    check_jax()
    check_torch()

if __name__ == "__main__":
    main()
