# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 6

# %% [markdown]
# 6. Se midió la temperatura de fusión de un aceite vegetal hidrogenado en una muestra de tamaño 16, y se encontró una media de 94.32. Si la temperatura de fusión sigue una distribución normal con una desviación estándar de 1.20. Probar a un 95% de nivel de confianza que la media se ha mantenido en 95.

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ = 95  
# H<sub>1</sub>: µ ≠ 95

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
x = 94.32
x

# %% [markdown]
# $\overline{x}$ = 94.32

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 95
mu

# %% [markdown]
# ${µ}$ = 95

# %% [markdown]
# #### Calculate ${s}$

# %%
s = 1.20
s

# %% [markdown]
# ${ s }$ = 1.20

# %% [markdown]
# #### Calculate ${n}$

# %%
n = 16

# %% [markdown]
# ${ n }$ = 16

# %% [markdown]
# #### Calculate ${ t }$

# %% [markdown]
# $$t = \frac{94.32-95}{\frac{1.20}{ \sqrt{16}}}$$

# %%
tc = (x-mu)/(s/math.sqrt(n))
tc

# %% [markdown]
# ${t}$ = -2.26

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = -2.26  
# t<sub>0.05</sub> = ${\pm}$ 2.13

# %%
t1 = 2.13
t2 = -2.13

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
# #### H<sub>0</sub> is rejected
# #### H<sub>1</sub> is accepted

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que media no se ha mantenido en 95. Con una muy ligera tendencia hacia la izquiera (es menor).
print('Con un 95% de confianza se puede concluir que media no se ha mantenido en 95. Con una muy ligera tendencia hacia la izquiera (es menor).')
