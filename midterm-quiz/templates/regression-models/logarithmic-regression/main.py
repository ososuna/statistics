import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

def logarithmicRegression(x, y):
  fit = np.polyfit(np.log(x), y, 1)
  y_pred = []
  for i in x:
    y_pred.append(fit[1] + fit[0] * np.log(i))
  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

logarithmicRegression(
  [2.50, 3, 4, 5, 5.5, 6, 7],
  [12.5, 10, 7, 4.50, 4, 3, 3.5]
)
