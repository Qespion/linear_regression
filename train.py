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
    """
    Estimate the price of a car with it mileage
    :param mileage:
    :param theta0:
    :param theta1:
    :return:
    """
    return theta0 + (theta1 * mileage)


def cost_function(X, Y, theta0, theta1):
    N = len(X)
    err = 0.0
    for i in range(N):
        err += (Y[i] - estimate_price(X[i], theta0, theta1)) ** 2
    return err / N


def gradient_descent(X, Y, theta0, theta1, lr):
    N = len(X)
    deriv_theta0 = 0
    deriv_theta1 = 0
    for i in range(N):
        deriv_theta0 += -2 * X[i] * (Y[i] - (estimate_price(X[i], theta0, theta1)))
        deriv_theta1 += -2 * (Y[i] - (estimate_price(X[i], theta0, theta1)))
    theta0 -= (deriv_theta0 / N) * lr
    theta1 -= (deriv_theta1 / N) * lr
    return theta0, theta1


def linear_regression(X, Y, theta0, theta1, lr=0.001, iters=10000):
    """
    The linear regression function
    FUCK THIS SHIT
    """
    cost_hist = []
    for i in range(iters):
        theta0, theta1 = gradient_descent(X, Y, theta0, theta1, lr)
        cost_hist.append(cost_function(X, Y, theta0, theta1))
        if i % 10 == 0:
            print("iter: " + str(i) + " cost: " + str(cost_hist))
    return theta0, theta1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=check_file_ext, help="CSV file path")
    args = parser.parse_args()
    data = np.genfromtxt(args.filename, delimiter=',', skip_header=1)
    X = data[:, 0]
    Y = data[:, 1]
    theta0 = 0
    theta1 = 0
    thetas = linear_regression(X, Y, theta0, theta1)
    print(thetas)
    np.savetxt("thetas.csv", thetas, delimiter=",")


if __name__ == "__main__":
    main()
