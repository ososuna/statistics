# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
weather_data_m = pd.read_csv('/home/ivanm/Desktop/repos/statistics/multiple-linear-regression/data/weatherHistory.csv', nrows=2000)
weather_data_m

# %%
weather_features = ['Temperature (C)','Wind Speed (km/h)', 'Pressure (millibars)']

X = weather_data_m[weather_features]
y = weather_data_m.Humidity

plt.subplot(2,2,1)
plt.scatter(X['Temperature (C)'], y)
plt.subplot(2,2,2)
plt.scatter(X['Wind Speed (km/h)'], y)
plt.subplot(2,2,3)
plt.scatter(X['Pressure (millibars)'], y)

# %%
X = X.drop('Pressure (millibars)', 1)
X

# %%
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = X['Temperature (C)']
x2 = X['Wind Speed (km/h)']

ax.scatter(x1, x2, y, c='r', marker='o')

ax.set_xlabel('Temperature (C)')
ax.set_ylabel('Wind Speed (km/h)')
ax.set_zlabel('Humidity')

# %%
from sklearn.linear_model import LinearRegression

mlr_model = LinearRegression()
mlr_model.fit(X, y)

# %%
theta0 = mlr_model.intercept_
theta1, theta2 = mlr_model.coef_
theta0, theta1, theta2

# %%
y_pred = mlr_model.predict([[15,21]])
y_pred


