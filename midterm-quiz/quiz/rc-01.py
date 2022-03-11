import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [1214, 1217, 1218, 1217, 1218, 1220, 1223, 1224, 1226, 1229, 1231, 1233, 1234]

def quadraticRegression(x, y):
  n = len(x)
  
  qm = np.poly1d(np.polyfit(x, y, 2))
  y_pred = qm(x)
  
  ss_tot = 0
  ss_res = 0
  mean_y = sum(y)/n

  for i in range(n):
    ss_tot += (y[i] - mean_y) ** 2
    ss_res += (y[i] - y_pred[i]) ** 2
  r2 = 1 - (ss_res/ss_tot)
  print("\nR2")
  print(r2)

  print(f'\ne. La confiabilidad del modelo es de: {r2}')
  print(f'\nf. Embarques para el año 15: {qm(15)}')

  print('\nb. Inserte la ecuación del gráfico, el valor de R2 y la línea de dispersión.')
  plt.scatter(x, y)
  plt.plot(x, y_pred, c='blue', linewidth=2)
  plt.show()

quadraticRegression(x, y)
