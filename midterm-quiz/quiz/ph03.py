import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency 
from scipy.stats import chi2
  
print('\na. ¿Cuáles son las hipótesis nulas y alternas?')
print('H0: independiente del género')
print('H1: dependiente del género')

print('\nb. ¿Qué nivel de significancia usarías y por qué?')
print('90% debido a que es un estudio social')
print('1 - α = 90%')
print('α = 10%')

print('\nc. ¿Cuál es el estadístico de prueba que usarás?')
print('Estadístico chi cuadrado')
print('Debido a que es una prueba de independencia')


# d, e, f
data = [[12, 10, 13, 19, 16], [15, 18, 15, 12, 14]] 
stat, p, dof, expected = chi2_contingency(data) 

alpha = 0.05
print("P valor es " + str(p)) 
if p <= alpha: 
  print('Dependent(Se rechaza H0)') 
else: 
  print('Independent(Se acepta H0)')

chi2 = chi2.ppf(1-.1, df = 11)
print(chi2)

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=p, color="blue")
plt.axvline(x=chi2, color="red")
plt.axvline(x=mu, color="green")
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
print('\nd, e, f')

print('\ng. Conclusiones')
print('Con un nivel de significancia del 90% se afirma que es indendiente el sabor del género')
