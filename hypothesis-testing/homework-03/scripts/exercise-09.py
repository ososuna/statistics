# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 9

# %% [markdown]
# 9. Un criador de pollos sabe por experiencia que el peso de los pollos de cinco meses es de 4.35 libras. Los pesos siguen una distribución normal. Para tratar de aumentar el peso de dichas aves se le agrega un aditivo al alimento. En una muestra de pollos en cinco meses se obtuvieron los siguientes pesos (en libras). 4.41 4.37 4.33 4.35 4.30 4.39 4.36 4.38 4.40 4.39  
# En el nivel de 0.01, ¿el aditivo ha aumentado el peso promedio de los pollos?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ ≤ 4.35  
# H<sub>1</sub>: µ > 4.35

# %% [markdown]
# ### 2. Define the level of confidence and significance

# %% [markdown]
# 1 - α = 99%  
# α = 1%

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
data = [4.41, 4.37, 4.33, 4.35, 4.30, 4.39, 4.36, 4.38, 4.40, 4.39]

# %%
x = sum(data) / len(data)
x

# %% [markdown]
# $\overline{x}$ = 4.368

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 4.35
mu

# %% [markdown]
# ${µ}$ = 4.35

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
# $ \Sigma|x-µ|^{2} $ = 0.0136

# %%
n = len(data)
n

# %% [markdown]
# ${N}$ = 10

# %% [markdown]
# $$ s = \sqrt{ \frac{0.0136}{10} } $$

# %%
s = math.sqrt(sum(avgDistance)/n)
s

# %% [markdown]
# ${ s }$ = 0.037

# %% [markdown]
# #### Calculate ${n}$

# %%
n

# %% [markdown]
# ${ n }$ = 10

# %% [markdown]
# #### Calculate ${ t }$

# %% [markdown]
# $$t = \frac{4.368-2.35}{\frac{0.0136}{ \sqrt{10}}}$$

# %%
tc = (x-mu)/(s/math.sqrt(n))
tc

# %% [markdown]
# ${t}$ = 1.54

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = 1.54  
# t<sub>0.01</sub> = 2.821

# %%
t = 2.821

# %% [markdown]
# ### 6. Take decision rule

# %%
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=tc, color="blue")
plt.axvline(x=t, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["tc", "t0.01", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 99% de confianza se puede concluir que el aditivo NO ha aumentado el peso promedio de los pollos.
print('Con un 99% de confianza se puede concluir que el aditivo NO ha aumentado el peso promedio de los pollos.')
