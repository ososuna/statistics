import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 1. Define the null and alternate hypotheses
print('H0: no diferences between given data')
print('H1: diferences between given data')

# 2. Define the level of confidence and significance
print('1 - α = 95%')
print('α = 5%')
confidence = 0.05

# 3. Select the test statistic
print('anova')

# 4. Calculate the test statistic
data = [
  {
    'id': 1,
    'data': [15, 16, 14, 15, 17]
  },
  {
    'id': 2,
    'data': [14, 13, 15, 16, 14]
  },
  {
    'id': 3,
    'data': [13, 12, 11, 14, 11]
  }
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
  print(f'critical value: {criticalValue}')
  print(f'f: {f}')
  print(f)
  # 5. Acceptance and rejection region
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

# 6. Set decision rule
print('H0 is rejected')
print('H1 is accepted')

# 7. Draw conclusions
print('With a confidence level of 95% it is affirmed that there are differences between the groups')
