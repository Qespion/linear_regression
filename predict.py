#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
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


def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--thetas", help="CSV thetas file", type=check_file_ext, required=False)
    args = parser.parse_args()
    thetas = [0, 0]
    if args.thetas is not None:
        thetas = np.genfromtxt(args.thetas)
    mileage = float(input("Enter a mileage for estimation: "))
    print(estimate_price(mileage, thetas[0], thetas[1]))


if __name__ == "__main__":
    main()
