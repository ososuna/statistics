import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

def logarithmicRegression(x, y):
  
  n = len(x)
  fit = np.polyfit(np.log(x), y, 1)

  # Obtain R2
  y_pred = []
  for i in x:
    y_pred.append(fit[1] + fit[0] * np.log(i))
  
  ss_tot = 0
  ss_res = 0
  mean_y = sum(y)/n

  for i in range(n):
    ss_tot += (y[i] - mean_y) ** 2
    ss_res += (y[i] - y_pred[i]) ** 2
  r2 = 1 - (ss_res/ss_tot)
  print("R2 Score")
  print(r2)
  
  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

logarithmicRegression(
  [2.50, 3, 4, 5, 5.5, 6, 7],
  [12.5, 10, 7, 4.50, 4, 3, 3.5]
)
