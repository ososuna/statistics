import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.api as sm

def linearRegressionStatsModels(x, y):
  X = sm.add_constant(x)
  model = sm.OLS(y,X)
  results = model.fit()
  results.summary()

  coef = results.params[1]
  intercept = results.params[0]

  ec = f"y = {coef} x + {intercept}"
  y_pred = results.predict(X)

  plt.scatter(x, y); plt.xlabel('x'); plt.ylabel('y');
  plt.plot(x, y_pred, c='red', linewidth=2)
  plt.text(23, 10, ec)
  plt.show()

def linearRegressionLeastSquare(x, y):
  n = len(x)

  # Finding required sum for least square methods
  sumX,sumX2,sumY,sumXY = 0,0,0,0
  for i in range(n):
      sumX = sum(x)
      sumX2 = sum([i ** 2 for i in x])
      sumY = sum(y)
      sumXY = sum([x * y for (x, y) in zip(x, y)])

  # Obtaining a and b
  b = (n * sumXY - sumX * sumY)/(n*sumX2 - sumX * sumX)
  a = (sumY - b*sumX)/n

  # Displaying coefficients a, b & equation
  print("\nCoefficients are:")
  print("a: ", a)
  print("b: ", b)

  print("\nEquation is:")
  print(f'y = {a} + {b}x')

  # Obtain R2
  y_pred = []
  for i in range(n):
    y_pred.append(a+b*x[i])
  
  ss_tot = 0
  ss_res = 0
  mean_y = sum(y)/n

  for i in range(n):
    ss_tot += (y[i] - mean_y) ** 2
    ss_res += (y[i] - y_pred[i]) ** 2
  r2 = 1 - (ss_res/ss_tot)
  print("R2 Score")
  print(r2)

  # Plot regression model
  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

linearRegressionLeastSquare(
  [16, 32, 48, 56, 64, 80],
  [10, 15, 20, 22, 30, 32]
)
