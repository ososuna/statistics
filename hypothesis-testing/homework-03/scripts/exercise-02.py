# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 2

# %% [markdown]
# 2. Un estudio encontró que 40% de los usuarios de Internet recibieron más de 10 mensajes diarios. Si de 420 usuarios 188 recibieron estos mensajes, y con un nivel de significancia del 5% ¿Cuál es la conclusión?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: ${π}$  = 40%  
# H<sub>1</sub>: ${π}$  ≠ 40%

# %% [markdown]
# ### 2. Define the level of confidence and significance

# %% [markdown]
# 1 - α = 95%  
# α = 5%

# %% [markdown]
# ### 3. Select the test statistic

# %% [markdown]
# $$Z = \frac{p-π}{\sqrt{\frac{π(1-π)}{n}}}$$

# %% [markdown]
# _Where:_  
# ${Z}$ = test statistic  
# ${p}$ = sample proportion  
# ${π}$ = proportion  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# ${p}$ = 0.448

# %% [markdown]
# ${π}$ = 0.40

# %% [markdown]
# ${ n }$ = 420

# %%
p = 0.448
pi = 0.40
n = 420

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{0.448-0.40}{\sqrt{\frac{0.40(1-0.40)}{420}}}$$

# %%
Zc = (p-pi)/math.sqrt((pi*(1-pi))/n)
Zc

# %% [markdown]
# ${Z}$ = 2.01

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = 2.01  
# Z<sub>0.05</sub> = ${\pm}$ 1.96

# %%
Z1 = -1.96
Z2 = 1.96

# %% [markdown]
# ### 6. Take decision rule

# %%
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z1, color="red")
plt.axvline(x=Z2, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z-0.01", "Z0.01", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is rejected
# #### H<sub>1</sub> is accepted

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que la proporción de usuarios que reciben 10 mensajes diarios es diferente al 40%. En esta prueba de hipótesis se demuestra que es ligeramente mayor.
print('Con un 95% de confianza se puede concluir que la proporción de usuarios que reciben 10 mensajes diarios es diferente al 40%. En esta prueba de hipótesis se demuestra que es ligeramente mayor.')
