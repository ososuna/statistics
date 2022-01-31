import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

p = 0.02
pi = 0.05
n = 200

Zc = (p-pi)/math.sqrt((pi*(1-pi))/n)
Zc

Z = 2.33

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z0.01", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

print('Con un 99% de confianza se puede concluir que la proporción de controladores defectuosos no es mayor a 5%.')
