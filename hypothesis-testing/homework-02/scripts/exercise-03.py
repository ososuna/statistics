import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

p = 0.44
pi = 0.30
n = 70

Zc = (p-pi)/math.sqrt((pi*(1-pi))/n)
Zc

Z1 = -1.64
Z2 = 1.64

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z1, color="red")
plt.axvline(x=Z2, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z-0.01", "Z0.01", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

print('Con un 90% de confianza se puede concluir que la proporción de estudiantes mujeres en ingeniería es diferente a 30%.')
