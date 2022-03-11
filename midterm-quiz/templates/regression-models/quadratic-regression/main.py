import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

def quadraticRegression(x, y):
  qm = np.poly1d(np.polyfit(x, y, 2))
  y_pred_q = qm(x)
  plt.scatter(x, y)
  plt.plot(x, y_pred_q, c='blue', linewidth=2)
  plt.show()

quadraticRegression(
  [2.50, 3, 4, 5, 5.5, 6, 7],
  [12.5, 10, 7, 4.50, 4, 3, 3.5]
)
