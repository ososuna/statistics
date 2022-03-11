import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

def potentialRegression(x, y):
  n = len(x)

  # Finding required sum for least square methods
  sumX,sumX2,sumY,sumXY = 0,0,0,0
  for i in range(n):
      sumX = sumX + np.log(x[i])
      sumX2 = sumX2 +np.log(x[i])*np.log(x[i])
      sumY = sumY + np.log(y[i])
      sumXY = sumXY + np.log(x[i])*np.log(y[i])

  # Finding coefficients A and B
  b = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
  A = (sumY - b*sumX)/n

  # Obtaining a and b
  a = np.exp(A)

  # Displaying coefficients a, b & equation
  print("\nCoefficients are:")
  print("a: ", a)
  print("b: ", b)

  print("\nEquation is:")
  print(f'y = {a}x ^ {b}')

  # Plot regression model
  y_pred = []
  for i in range(n):
    y_pred.append(a*x[i]**b)

  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

potentialRegression(
  [61, 26, 7, 2.6],
  [350, 400, 500, 600]
)
