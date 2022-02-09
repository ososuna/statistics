# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 4

# %% [markdown]
# 4. Un gerente de un restaurante planea una oferta especial si más del 15% de los clientes compra vasos de diseño especial con personajes de caricaturas. En una prueba realizada por el gerente del restaurante, 88 de 500 clientes compraron vasos con ese diseño especial. A un 0.01 de nivel de significancia, ¿Cuál es su recomendación?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: ${π}$ ≤ 15%  
# H<sub>1</sub>: ${π}$ > 15%

# %% [markdown]
# ### 2. Define the level of confidence and significance

# %% [markdown]
# 1 - α = 99%  
# α = 1%

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
# ${p}$ = 0.176

# %% [markdown]
# ${π}$ = 0.15

# %% [markdown]
# ${ n }$ = 500

# %%
p = 0.176
pi = 0.15
n = 500

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{0.176-0.15}{\sqrt{\frac{0.15(1-0.15)}{500}}}$$

# %%
Zc = (p-pi)/math.sqrt((pi*(1-pi))/n)
Zc

# %% [markdown]
# ${Z}$ = 1.62

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = 1.62  
# Z<sub>0.01</sub> = 2.33

# %%
Z = 2.33

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
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 99% de confianza se puede concluir que menos del 15% de los clientes compra vasos de diseño especial con personajes de caricaturas.
print('Con un 99% de confianza se puede concluir que menos del 15% de los clientes compra vasos de diseño especial con personajes de caricaturas.')
