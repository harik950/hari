# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144ROsznwNTOaUTOUKEb76TE2O-izqLEj
"""

import matplotlib.pyplot as mlp
import pandas as pd
import io
from google.colab import files
uploaded=files.upload()

dataset =pd.read_csv('Salary_Data.csv')
dataset.head()
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train ,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
y_pred

mlp.scatter(x_train,y_train,color='red')
mlp.plot(x_train,regressor.predict(x_train),color='blue')

mlp.title("Salary vsExperience (Training set)")

mlp.xlabel("Years of experience")
mlp.ylabel("Salaries")
mlp.show()

mlp.scatter(x_test,y_test,color='red')
mlp.plot(x_train,regressor.predict(x_train),color='blue')