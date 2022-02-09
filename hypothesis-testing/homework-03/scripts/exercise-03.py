# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 3

# %% [markdown]
# 3. Un estudio indicó que el 64% de los consumidores de supermercado creen en las marcas propias. El fabricante de una salsa de tomate preguntó a 100 compradores donde 52 prefieren marca propia, probar si el porcentaje de preferencias es menor al 64%, para un 5% de nivel de significancia.

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: ${π}$ ≥ 64%  
# H<sub>1</sub>: ${π}$ < 64%

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
# ${ Z }$ = test statistic  
# ${p}$ = sample proportion  
# ${π}$ = proportion  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# ${p}$ = 0.52

# %% [markdown]
# ${π}$ = 0.64

# %% [markdown]
# ${ n }$ = 100

# %%
p = 0.52
pi = 0.64
n = 100

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{0.52-0.64}{\sqrt{\frac{0.64(1-0.64)}{100}}}$$

# %%
Zc = (p-pi)/math.sqrt((pi*(1-pi))/n)
Zc

# %% [markdown]
# ${Z}$ = -2.5

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = -2.5  
# Z<sub>0.05</sub> = -1.64

# %%
Z = -1.64

# %% [markdown]
# ### 6. Take decision rule

# %%
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.axvline(x=Zc, color="blue")
plt.axvline(x=Z, color="red")
plt.axvline(x=mu, color="green")
plt.legend(["Zc", "Z0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is rejected
# #### H<sub>1</sub> is accepted

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que la proporción de los consumidores de supermercado que creen en las marcas propias es menor al 64%.
print('Con un 95% de confianza se puede concluir que la proporción de los consumidores de supermercado que creen en las marcas propias es menor al 64%.')
