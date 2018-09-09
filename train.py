#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import argparse
import matplotlib.pyplot as plt


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
    return theta0 + theta1 * mileage


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
        deriv_theta0 += -2 * X[i] * (Y[i] - (theta0 * X[i] + theta1))     
        deriv_theta1 += -2 * (Y[i] - (theta0 * X[i] + theta1))        
    theta0 = theta0 - lr * (deriv_theta0 / float(len(X)))
    theta1 = theta1 - lr * (deriv_theta1 /  float(len(X)))
    return theta0, theta1


def linear_regression(X, Y,lr=0.001, iters=10000):
    """
    The linear regression function
    FUCK THIS SHIT
    """
    theta0 = 0
    theta1 = 0
    loss = []
    for i in range(iters):
        theta0, theta1 = gradient_descent(X, Y, theta0, theta1, lr)
        loss.append(cost_function(X, Y, theta0, theta1))
    return theta0, theta1, loss


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=check_file_ext, help="CSV file path")
    args = parser.parse_args()
    data = np.genfromtxt(args.filename, delimiter=',', skip_header=1)
    data = data / 100000
    X = data[:, 0]
    Y = data[:, 1]
    theta0, theta1, loss = linear_regression(X, Y)
    theta1 *= 100000
    line_x = [min(X * 100000), max(X * 100000)]
    line_y = [(theta0 * i) + theta1 for i in line_x]
    plt.plot(line_x, line_y, 'b')
    plt.plot(X * 100000, Y * 100000, 'ro')
    plt.show()
    print('Final loss = ', loss[-1])
    print('Thetas = ', [theta1, theta0])
    np.savetxt("thetas.csv", [theta1, theta0], delimiter=",")


if __name__ == "__main__":
    main()
