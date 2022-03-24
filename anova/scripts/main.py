import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

confidence=0.1
data = [
  {
    'id': 'a',
    'data': [5, 2, 7, 6, 9, 2, 1, 8]
  },
  {
    'id': 'b',
    'data': [6, 5, 8, 6, 2, 2, 1, 9]
  },
  {
    'id': 'c',
    'data': [7, 7, 6, 5, 4, 2, 3, 1]
  },
  {
    'id': 'd',
    'data': [9, 6, 7, 1, 5, 9, 4, 6]
  },
  {
    'id': 'e',
    'data': [8, 10, 8, 4, 6, 6, 9, 9]
  },
]

def anova_test(data=[{}], confidence=0.05):
  n = sum([ len(i['data']) for i in data ])
  x_tested = sum([ sum(i['data']) for i in data ])/n
  lg = n-1
  xi_x = []
  for i in data:
    xi_x.append([ (j-x_tested)**2 for j in i['data'] ])
    scTotal = sum([ sum(j) for j in xi_x ])
  glEntre = len(data)-1
  avg = []
  for i in data:
    avg.append( sum([ j for j in i['data']])/len(i['data']) )
    scEntre = sum([ len(i['data']) * (j - x_tested)**2 for j in avg ])
  s2e = scEntre/glEntre
  glIntra=n-len(data)
  xi_avg = []
  for i in data:
    xi_avg.append([ (j - sum([ j for j in i['data']])/len(i['data']) )**2 for j in i['data'] ])
    scIntra = sum([ sum(j) for j in xi_avg ])
  s2r = scIntra/glIntra
  f = s2e/s2r
  gl = [scEntre, scIntra]
  criticalValue =  stats.f.isf(confidence, scEntre, scIntra)
  mu = 0
  variance = 1
  sigma = math.sqrt(variance)
  x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
  plt.axvline(x=f, color="blue")
  plt.axvline(x=criticalValue, color="red")
  plt.axvline(x=mu, color="green")
  plt.legend(["f", "critical value", "µ"])
  plt.plot(x, stats.norm.pdf(x, mu, sigma))
  plt.show()

anova_test(data, confidence)
