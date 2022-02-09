# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 5

# %% [markdown]
# 5. Las rentas diarias de automóviles en dólares de ocho ciudades se muestra a continuación:

# %% [markdown]
# | Ciudad     | A  | B  | C  | D  | E  | F  | G  | H  |
# | ---------- | -  | -  | -  | -  | -  | -  | -  | -  |
# | Renta      | 47 | 50 | 53 | 45 | 40 | 43 | 39 | 37 |
# 

# %% [markdown]
# ¿A un 5% se comprueba la hipótesis de que la media de la población es de 45 dólares?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ = 45  
# H<sub>1</sub>: µ ≠ 45

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
# ${t}$ = test statistic  
# $\overline{x}$ = sample average  
# ${µ}$ = average  
# ${s}$ = sample standard deviation  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# #### Calculate $\overline{x}$

# %%
data = [47, 50, 53, 45, 40, 43, 39, 37]

# %%
x = sum(data) / len(data)
x

# %% [markdown]
# $\overline{x}$ = 44.25

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 45
mu

# %% [markdown]
# ${µ}$ = 45

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
# $ \Sigma|x-µ|^{2} $ = 222

# %%
n = len(data)
n

# %% [markdown]
# ${N}$ = 8

# %% [markdown]
# $$ s = \sqrt{ \frac{222}{8} } $$

# %%
s = math.sqrt(sum(avgDistance)/n)
s

# %% [markdown]
# ${ s }$ = 5.27

# %% [markdown]
# #### Calculate ${n}$

# %%
n

# %% [markdown]
# ${ n }$ = 8

# %% [markdown]
# #### Calculate ${ t }$

# %% [markdown]
# $$t = \frac{44.25-45}{\frac{5.27}{ \sqrt{8}}}$$

# %%
tc = (x-mu)/(s/math.sqrt(n))
tc

# %% [markdown]
# ${t}$ = -0.40

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = -0.40  
# t<sub>0.05</sub> = ${\pm}$ 2.365

# %%
t1 = 2.365
t2 = -2.365

# %% [markdown]
# ### 6. Take decision rule

# %%
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=tc, color="blue")
plt.axvline(x=t1, color="red")
plt.axvline(x=t2, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["tc", "t-0.05", "t0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que la media de la población es de 45 dólares.
print('Con un 95% de confianza se puede concluir que la media de la población es de 45 dólares.')
