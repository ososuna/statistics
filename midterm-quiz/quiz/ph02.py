import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

print('\na. ¿Cuáles son las hipótesis nulas y alternas?')
print('H0: π = 70')
print('H1: π != 70')

print('\nb. ¿Qué nivel de significancia usarías y por qué?')
print('90% debido a que es un estudio social')
print('1 - α = 90%')
print('α = 10%')

print('\nc. ¿Cuál es el estadístico de prueba que usarás?')
print('Estadístico Z')
print('Debido a que es una prueba de hipótesis sobre la proporción')


# d, e, f
mData = [20, 33, 25, 40, 15, 15, 20]
wData = [45, 45, 48, 60, 25, 30, 40]

sumTotal = sum(mData) + sum(wData)
p = 63.55
pi = 70
n = 7
Zc = (p-pi)/(math.sqrt((pi*(100-pi))/n))

Z = 1.64

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z, color="red")
plt.axvline(x=-Z, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z0.1", "Z-0.1", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
print('\nd, e, f')

print('\ng. Conclusiones')
print('Con un nivel de significancia del 90% se afirma que el el 70% de su clientela son mujeres')
