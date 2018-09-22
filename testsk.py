#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
import numpy as np

Vp = 13
#Reads the dataset
df = pd.read_csv('data_test.txt', names=['X','Y'])

#Divides the data into train and test sets
X_train, X_test, y_train, y_test = np.asarray(tts(df['X'], df['Y'], test_size=0.1))

#Trains our model
reg = LinearRegression()
reg.fit(X_train.values.reshape(-1,1), y_train.values.reshape(-1,1))

#Print Score and prediction
print('Score: ', reg.score(X_test.values.reshape(-1,1), y_test.values.reshape(-1,1)))
print('Value Predicted for X = ', Vp, ':', reg.predict(14.164))

#Plot regression
x_line = np.arange(5,25).reshape(-1,1)
sea.regplot(x='X', y='Y', data=df, fit_reg=False)
plt.plot(x_line, reg.predict(x_line))
plt.show()