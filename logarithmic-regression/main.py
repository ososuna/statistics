import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.api as sm

# x = [4, 8, 12, 14, 18, 23, 28, 32]
# y = [240, 200, 150, 130, 100, 80, 60, 30]

# fit = np.polyfit(np.log(x), y, 1)
# print(fit)

# y_pred = []

# for i in x:
#   y_pred.append(fit[1] + fit[0] * np.log(i))


# plt.scatter(x, y)
# plt.plot(x, y_pred)
# plt.show()

# x = [1, 2, 5, 15, 25, 30, 35, 40]
# y = [99, 95, 85, 55, 30, 24, 20, 15]

# print(len(x), len(y))

x = [2.50, 3, 4, 5, 5.5, 6, 7]
y = [12.5, 10, 7, 4.50, 4, 3, 3.5]
print(len(x), len(y))

# Linear regression
X = sm.add_constant(x)

model = sm.OLS(y,X)
results = model.fit()

y_pred_l = results.predict(X)

# Quadratic regression
qm = np.poly1d(np.polyfit(x, y, 2))
y_pred_q = qm(x)

# Logarithmic regression
fit = np.polyfit(np.log(x), y, 1)
y_pred_log = []
for i in x:
  y_pred_log.append(fit[1] + fit[0] * np.log(i))

plt.scatter(x, y)
plt.plot(x, y_pred_l, c='red', linewidth=2)
plt.show()

plt.scatter(x, y)
plt.plot(x, y_pred_q, c='blue', linewidth=2)
plt.show()

plt.scatter(x, y)
plt.plot(x, y_pred_log, c='green', linewidth=2)
plt.show()
