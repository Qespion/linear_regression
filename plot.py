#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import argparse


def check_file_ext(filename):
    """
    Check file extension
    :param filename:
    :return filename:
    """
    if not filename.endswith('.csv'):
        raise argparse.ArgumentTypeError('wrong filetype or path')
    return filename


def plot(data):
    """
    Plot the data
    :param data:
    """
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Price on km")
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=check_file_ext, help="CSV file path")
    args = parser.parse_args()
    data = np.genfromtxt(args.filename, delimiter=',', skip_header=1)
    plot(data)


if __name__ == "__main__":
    main()
