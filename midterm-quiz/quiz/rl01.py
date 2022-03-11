import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.api as sm

x = [710, 929, 314, 504, 619, 518, 417, 205, 438, 545, 647, 694]
y = [65, 43, 29, 47, 52, 50, 46, 29, 31, 43, 49, 64]


def linearRegressionLeastSquare(x, y):
  n = len(x)
  
  print('\nf, g, h')
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

  ec = f'y = {a} + {b}x'
  print("\nb. Ecuación:")
  print(ec)

  print(f'\ni. De tener 90 rentas, el ingreso es de: {a+b*90}')

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
  print("\nb. R2")
  print(r2)

  # Plot regression model
  print('a. Diagrama dispersión y línea de tendencia')
  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

linearRegressionLeastSquare(x, y)

print('\nc. Variable independiente: rentas')
print('\nd. Variable dependiente: ingreso')
print('\ne. Relación indirecta, ya que el valor de R2 para la regresión lineal es de: 0.42')
