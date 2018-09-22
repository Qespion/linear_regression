#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import argparse
import matplotlib.pyplot as plt


def main():
    tup1 = ('as simple', 42, 'as that')
    d = {}
    d['test'] = 42
    d['autre essai'] = 'plusierus', 'keys'
    print(tup1)
    print(d['autre essai'][1])

if __name__ == "__main__":
    main()