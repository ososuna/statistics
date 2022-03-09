import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.api as sm

def linearRegression(x, y):
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

linearRegression(
  [16, 32, 48, 56, 64, 80],
  [10, 15, 20, 22, 30, 32]
)
