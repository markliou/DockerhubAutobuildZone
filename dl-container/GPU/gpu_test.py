#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tensorflow as tf
import jax
import torch


def check_tf():
    assert (len(tf.config.list_physical_devices('GPU')) > 0)


def check_jax():
    assert (jax.devices()[0].platform != 'cpu')


def check_torch():
    assert (torch.cuda.is_available())


def main():
    check_tf()
    check_jax()
    check_torch()


if __name__ == "__main__":
    main()
