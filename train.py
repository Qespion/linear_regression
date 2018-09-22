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


def normalize_data(X, Y):
    norm_X = []
    norm_Y = []
    for i in X:
        i = (i - min(X)) / (max(X) - min(X))
        norm_X.append(i)
    for i in Y:
        i = (i - min(X)) / (max(X) - min(X))
        norm_Y.append(i)
    return norm_X, norm_Y

def rev_normalize(X, norm_X, theta0):
    return theta0 * (max(X) - min(X)) + min(X)


def cost_function(X, Y, theta0, theta1):
    N = len(X)
    err = 0
    for i in range(N):
        err += (Y[i] - estimate_price(X[i], theta0, theta1)) ** 2
    return err / N


def gradient_descent(X, Y, theta0, theta1):
    M = len(X)
    derivee_theta_0 = float(0)
    derivee_theta_1 = float(0)
    for i in range(0, len(X)):
        derivee_theta_0 += float(((theta0 + (theta1 * X[i])) - float(Y[i])))
        derivee_theta_1 += (((theta0 + (theta1 * X[i]))) - float(Y[i])) * float(X[i])
    derivee_theta_0 = (1/M) * derivee_theta_0
    derivee_theta_1 = (1/M) * derivee_theta_1
    return [derivee_theta_0, derivee_theta_1]


def new_thetas(X, Y, theta0, theta1, lr):
    [derivee_theta_0, derivee_theta_1] = gradient_descent(X, Y, theta0, theta1)
    nouvelle_theta_0 = theta0 - (lr * derivee_theta_0)
    nouvelle_theta_1 = theta1 - (lr * derivee_theta_1)
    return [nouvelle_theta_0,nouvelle_theta_1]

def linear_regression(X, Y,lr=0.001, iters=100000):
    """
    The linear regression function
    FUCK THIS SHIT
    """
    theta0 = 0
    theta1 = 0
    loss = []
    for _ in range(iters):
        theta0, theta1 = new_thetas(X, Y, theta0, theta1, lr)
        loss.append(cost_function(X, Y, theta0, theta1))
    return theta0, theta1, loss


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=check_file_ext, help="CSV file path")
    args = parser.parse_args()
    data = np.genfromtxt(args.filename, delimiter=',', skip_header=1)
    X = data[:, 0]
    Y = data[:, 1]
    norm_X, norm_Y = normalize_data(X, Y)
    theta0, theta1, loss = linear_regression(norm_X, norm_Y)
    theta0 = rev_normalize(X, norm_X, theta0)
    line_x = [min(X), max(X)]
    line_y = [(theta1 * i) + theta0 for i in line_x]
    plt.plot(line_x, line_y, 'b')
    plt.plot(X, Y, 'ro')
    plt.show()
    print('Final loss = ', loss[-1])
    print('Thetas = ', [theta0, theta1])
    np.savetxt("thetas.csv", [theta0, theta1], delimiter=",")


if __name__ == "__main__":
    main()
