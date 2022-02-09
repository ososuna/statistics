# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 1

# %% [markdown]
# 1. Se supone que las ganancias por cierta acción bursátil son de 3 dólares. Una muestra de datos arrojó los resultados siguientes: 1.92, 2.16, 3.63, 3.16, 4.02, 3.14, 2.2, 2.34, 3.05, 2.38. Con un 95% de confianza probar esta afirmación

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ = 3  
# H<sub>1</sub>: µ ≠ 3

# %% [markdown]
# ### 2. Define the level of confidence and significance

# %% [markdown]
# 1 - α = 95%  
# α = 5%

# %% [markdown]
# ### 3. Select the test statistic

# %% [markdown]
# $$t = \frac{\overline{x}-µ}{\frac{s}{ \sqrt{n}}}$$

# %% [markdown]
# _Where:_  
# ${ t }$ = test statistic  
# $\overline{x}$ = sample average  
# ${µ}$ = average  
# ${s}$ = sample standard deviation  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# #### Calculate $\overline{x}$

# %%
data = [1.92, 2.16, 3.63, 3.16, 4.02, 3.14, 2.2, 2.34, 3.05, 2.38]

# %%
x = sum(data) / len(data)
x

# %% [markdown]
# $\overline{x}$ = 2.8

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 3
mu

# %% [markdown]
# ${µ}$ = 3

# %% [markdown]
# #### Calculate ${s}$

# %% [markdown]
# $$s = \sqrt{ \frac{\Sigma|x-µ|^{2}}{N} } $$

# %%
avgDistance = []
for i in data:
  avgDistance.append(abs(i-mu)**2)
sum(avgDistance)

# %% [markdown]
# $ \Sigma|x-µ|^{2} $ = 4.82

# %%
n = len(data)
n

# %% [markdown]
# ${N}$ = 10

# %% [markdown]
# $$ s = \sqrt{ \frac{4.82}{10} } $$

# %%
s = math.sqrt(sum(avgDistance)/n)
s

# %% [markdown]
# ${ s }$ = 0.69

# %% [markdown]
# #### Calculate ${n}$

# %%
n

# %% [markdown]
# ${ n }$ = 10

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{2.8-3}{\frac{0.69}{ \sqrt{10}}}$$

# %%
Zc = (x-mu)/(s/math.sqrt(n))
Zc

# %% [markdown]
# ${Z}$ = -0.91

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = -0.911  
# t<sub>0.05</sub> = ${\pm}$ 1.833

# %%
t1 = 1.83
t2 = -1.83

# %% [markdown]
# ### 6. Take decision rule

# %%
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=t1, color="red")
plt.axvline(x=t2, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z-0.05", "Z0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que las ganancias por cierta acción bursátil son de 3 dólares.
print('Con un 95% de confianza se puede concluir que las ganancias por cierta acción bursátil son de 3 dólares.')
