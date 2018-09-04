#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse

def check_file_ext(filename):
	if not filename.endswith('.csv'):
		raise argparse.ArgumentTypeError('wrong filetype or path')
	return filename

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=check_file_ext, help="CSV file path")
args = parser.parse_args()

with open(args.filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    km = []
    price = []
    for lines in reader:
        km.append(float(lines['km']))
        price.append(float(lines['price']))
    print(price)

plt.scatter(km, price)
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title("A l\'arrache")
plt.show()
