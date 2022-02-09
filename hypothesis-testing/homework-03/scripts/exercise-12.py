# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 12

# %% [markdown]
# 12. Una compañía desea comparar el aumento de peso en bebés que consumen su producto contra los que consumen el competidor. Una muestra de 40 bebés de usan la 1ª marca reveló un aumento de peso de 3.2 kg en los primeros tres meses después de nacidos con 1.2 kg de desviación estándar Una muestra de 55 bebés que usan la 2ª marca indica un aumento de 4.2 kg con desviación estándar de 1.4 kg. Con un nivel de significancia de 0.05 ¿Es posible concluir que los bebés que consumieron el producto de la marca 2 ganaron más peso?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ<sub>1</sub> ≥ µ<sub>2</sub>  
# H<sub>1</sub>: µ<sub>1</sub> < µ<sub>2</sub>

# %% [markdown]
# ### 2. Define the level of confidence and significance

# %% [markdown]
# 1 - α = 95%  
# α = 5%

# %% [markdown]
# ### 3. Select the test statistic

# %% [markdown]
# $$Z = \frac{\overline{x}_1-\overline{x}_2}{\sqrt{\frac{s_1^2}{ n_1}+\frac{s_2^2}{ n_2}}}$$

# %% [markdown]
# _Where:_  
# ${ Z }$ = test statistic  
# $\overline{x}$ = sample average  
# ${s}$ = sample standard deviation  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# #### Calculate $\overline{x}$

# %%
x1 = 3.2

# %%
x2 = 4.2

# %% [markdown]
# $\overline{x}$<sub>1</sub> = 3.2  
# $\overline{x}$<sub>2</sub> = 4.2

# %% [markdown]
# #### Calculate ${s}$

# %%
s1 = 1.2

# %%
s2 = 1.4

# %% [markdown]
# ${ s }$<sub>1</sub> = 1.2  
# ${ s }$<sub>2</sub> = 1.4

# %% [markdown]
# #### Calculate ${n}$

# %%
n1 = 40

# %%
n2 = 55

# %% [markdown]
# ${ n }$<sub>1</sub> = 40  
# ${ n }$<sub>2</sub> = 55

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{3.2-4.2}{\sqrt{\frac{1.2^2}{40}+\frac{1.4^2}{55}}}$$

# %%
Zc = (x1-x2)/(math.sqrt((s1**2/n1)+(s2**2/n2)))
Zc

# %% [markdown]
# ${Zc}$ = -3.74

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = -3.74  
# Z<sub>0.01</sub> = -1.64

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
# Con un 99% de confianza se puede concluir que los bebés que consumieron el producto de la marca 2 ganaron más peso.
print('Con un 99% de confianza se puede concluir que los bebés que consumieron el producto de la marca 2 ganaron más peso.')
