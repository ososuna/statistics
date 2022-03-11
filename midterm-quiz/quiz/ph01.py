import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def standardDeviation(data):
  avgDistance = []
  for i in data:
    avgDistance.append(abs(i-avg)**2)
  return math.sqrt(sum(avgDistance)/len(data))

print('\na. ¿Cuáles son las hipótesis nulas y alternas?')
print('H0: >= 22')
print('H1: < 22')

print('\nb. ¿Qué nivel de significancia usarías y por qué?')
print('99% debido a que es un estudio de calidad y producción')
print('1 - α = 99%')
print('α = 1%')

print('\nc. ¿Cuál es el estadístico de prueba que usarás?')
print('Estadístico t')
print('Debido a que es una prueba de hipótesis sobre la media de muestras pequeñas(<30)')


# d, e, f
data = [19.99, 20.75, 22.01, 22, 21.85, 21.10, 22.10, 22.30, 22.50, 22.10]
avg = sum(data) / len(data)
mu = 22
s = standardDeviation(data)
n = len(data)
tc = (avg-mu)/(s/math.sqrt(n))
t = -2.82
print(f'\nt calculada: {tc}')
print(f't: {t}')

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=tc, color="blue")
plt.axvline(x=t, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["tc", "t-0.01", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

print('\nd, e, f')

print('\ng. Conclusiones')
print('Con un nivel de significancia del 99% se afirma que el precio de la gasolina será de al menos 22 pesos por litro la siguiente semana')
