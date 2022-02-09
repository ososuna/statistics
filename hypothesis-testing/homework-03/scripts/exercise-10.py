# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 10

# %% [markdown]
# 10. Una empresa que se dedica a hacer encuestas se queja de que un agente realiza en promedio 53 encuestas por semana. Se ha introducido una forma más moderna de realizar las encuetas y la empresa quiere evaluar su efectividad. Los números de encuestas realizadas en una semana por una muestra aleatoria de agentes son: 53, 57, 50, 55, 58, 54, 60, 52, 59, 62, 60, 60, 51, 59, 56.  
# En el nivel de significancia del 0.05, ¿puede concluirse que la cantidad media de entrevistas realizadas por los agentes es superior a 53 por semana?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ ≤ 53  
# H<sub>1</sub>: µ > 53

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
data = [53, 57, 50, 55, 58, 54, 60, 52, 59, 62, 60, 60, 51, 59, 56]

# %%
x = sum(data) / len(data)
x

# %% [markdown]
# $\overline{x}$ = 56.4

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 53
mu

# %% [markdown]
# ${µ}$ = 53

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
# $ \Sigma|x-µ|^{2} $ = 369

# %%
n = len(data)
n

# %% [markdown]
# ${N}$ = 15

# %% [markdown]
# $$ s = \sqrt{ \frac{369}{10} } $$

# %%
s = math.sqrt(sum(avgDistance)/n)
s

# %% [markdown]
# ${ s }$ = 4.96

# %% [markdown]
# #### Calculate ${n}$

# %%
n

# %% [markdown]
# ${ n }$ = 15

# %% [markdown]
# #### Calculate ${ t }$

# %% [markdown]
# $$t = \frac{56.4-53}{\frac{4.96}{ \sqrt{15}}}$$

# %%
tc = (x-mu)/(s/math.sqrt(n))
tc

# %% [markdown]
# ${t}$ = 2.65

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = 2.65  
# t<sub>0.01</sub> = 1.76

# %%
t = 1.76

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
# Con un 95% de confianza se puede concluir que la cantidad media de entrevistas realizadas por los agentes es superior a 53 por semana.
print('Con un 95% de confianza se puede concluir que la cantidad media de entrevistas realizadas por los agentes es superior a 53 por semana.')
