import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

x = 27800
mu = 28000
s = 1000
n = 64

Zc = (x-mu)/(s/math.sqrt(n))
Zc

Z = -2.33

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

print('Con un 99% de confianza se puede concluir que nueva gama de llantas en promedio dura al menos 28,000 km.')

