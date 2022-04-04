
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

estaturaMadre = [63,37,64,60,65,67,59,60,58,72,63,67,62,69,63,64,63,64,60,65]
estaturaPadre = [64,65,67,72,72,72,67,71,66,75,69,70,69,62,66,76,69,68,66,68]
estaturaHija = [58.6,64.7,65.3,61,65.4,67.4,60.9,63.1,60,71.1,62.2,67.2,63.4,68.4,62.2,64.7,59.6,61,64,65.4]
vInd = [estaturaMadre,estaturaPadre]


X = vInd
y = estaturaHija

plt.subplot(2,2,1)
plt.scatter(X[0], y)
plt.subplot(2,2,2)
plt.scatter(X[1], y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = X[0]
x2 = X[1]

ax.scatter(x1, x2, y, c='r', marker='o')

ax.set_xlabel('Estatura Madre')
ax.set_ylabel('Estatura Padre')
ax.set_zlabel('Estatura Hija')



mlr_model = LinearRegression()
mlr_model.fit(X, y)

theta0 = mlr_model.intercept_
theta1, theta2 = mlr_model.coef_
theta0, theta1, theta2

y_pred = mlr_model.predict([[15,21]])
y_pred
