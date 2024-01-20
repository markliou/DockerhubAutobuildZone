import tensorflow as tf 
import jax 
import torch 


def check_tf():
    assert(len(tf.config.list_physical_devices('GPU')) > 0)

def check_jax():
    assert(len(jax.devices()) > 0)


def check_torch():
    assert()


def main():
    check_tf()
    check_jax()
    check_torch()


if __name__ == "__main__":
    main()