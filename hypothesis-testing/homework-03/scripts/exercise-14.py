# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 14

# %% [markdown]
# 14. El jefe de personal de una gran empresa afirma que la diferencia de los promedios de antigüedad entre las obreras y obreros de la compañía es de 3.5 años. El presidente de la compañía considera que ésta diferencia es superior. Para comprobar dicha situación, se toma una muestra aleatoria de 40 obreras cuyo promedio de antigüedad es de 12.4 años con desviación estándar de 1.5 años y de un grupo de 45 obreros cuyo promedio de antigüedad es de 8.3 años con desviación estándar de 1.7 años. Comprobar la hipótesis con un nivel de significación del 5%.

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ<sub>1</sub> = µ<sub>2</sub>  
# H<sub>1</sub>: µ<sub>1</sub> ≠ µ<sub>2</sub>

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
# ${µ}$ = average  
# ${s}$ = sample standard deviation  
# ${n}$ = sample size

# %% [markdown]
# ### 4. Calculate the test statistic

# %% [markdown]
# #### Calculate $\overline{x}$

# %%
x1 = 12.4

# %%
x2 = 8.3

# %% [markdown]
# $\overline{x}$<sub>1</sub> = 12.4  
# $\overline{x}$<sub>2</sub> = 8.3

# %% [markdown]
# #### Calculate ${s}$

# %%
s1 = 1.5

# %%
s2 = 1.7

# %% [markdown]
# ${ s }$<sub>1</sub> = 1.5  
# ${ s }$<sub>2</sub> = 1.7

# %% [markdown]
# #### Calculate ${n}$

# %%
n1 = 40

# %%
n2 = 45

# %% [markdown]
# ${ n }$<sub>1</sub> = 40  
# ${ n }$<sub>2</sub> = 45

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{12.4-8.3}{\sqrt{\frac{1.5^2}{40}+\frac{1.7^2}{45}}}$$

# %%
Zc = (x1-x2)/(math.sqrt((s1**2/n1)+(s2**2/n2)))
Zc

# %% [markdown]
# ${Zc}$ = 15.51

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = 15.51  
# Z<sub>0.05</sub> = ${\pm}$ 1.96

# %%
Z1 = 1.96
Z2 = -1.96

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
plt.legend(["Zc", "Z0.05", "Z-0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is rejected
# #### H<sub>1</sub> is accepted

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que la diferencia es superior a 3.5 años.
print('Con un 95% de confianza se puede concluir que la diferencia es superior a 3.5 años.')
