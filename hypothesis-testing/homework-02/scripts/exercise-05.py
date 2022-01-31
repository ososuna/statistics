import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

data = [6.1, 6.5, 6.2, 5.1, 5.5, 5.7, 6, 5.8, 6.2, 6.3, 6, 5.9, 5.9, 6.2, 6.3, 6.3, 5.8, 5.9, 5.8, 5.7, 5.9, 6.1, 6.2, 6.3, 6, 5.7, 5.8, 5.8, 5.9, 6.1, 6.2, 6.2, 6.3, 6, 5.8]

x = sum(data) / len(data)
mu = 5.6

avgDistance = []
for i in data:
  avgDistance.append(abs(i-mu)**2)
sum(avgDistance)

n = len(data)

s = math.sqrt(sum(avgDistance)/n)

Zc = (x-mu)/(s/math.sqrt(n))
Z = 2.33

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

print('Con un 99% de confianza se puede concluir que el consumo medio de combustible en carretera es superior a los 5.6 litros sobre 100 km')
