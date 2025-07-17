#!/usr/bin/python3
# -*- coding: utf-8 -*-
import torch
import numpy as np


def check_torch():
    print("Checking torch gpu available...")
    assert (torch.cuda.is_available())

    # test pytorch
    sample = np.array([.1, .2, .3])
    print("Checking torch function ...")
    torchV = torch.FloatTensor(sample)
    assert(((torchV * 2).numpy() == (sample * 2).astype(np.float32)).all())

def main():
    check_torch()

if __name__ == "__main__":
    main()
