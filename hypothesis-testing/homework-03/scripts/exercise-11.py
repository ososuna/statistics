# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 11

# %% [markdown]
# 11. El artículo “Effect of Welding Procedure on Flux Cored Steel Wire Deposits” (N. Ramini de Rissone, I. de S. Bott y cols., en Science and Technology of Welding and Joining, 2003:113122) compara las propiedades de soldaduras hechas con dióxido de carbono como gas de protección con respecto a las de soldaduras hechas mediante una mezcla de argón y dióxido de carbono. Una propiedad estudiada era el diámetro de inclusiones, que son partículas incrustadas en la soldadura. Una muestra de 544 inclusiones en soldaduras hechas al usar argón como protección tiene un diámetro promedio de 0.37 mm, con desviación estándar de 0.25 mm. Una muestra de 581 inclusiones en soldaduras hechas al emplear dióxido de carbono como protección tiene diámetro promedio de 0.40 mm, con desviación estándar de 0.26 mm. (Las desviaciones estándar se calcularon con una gráfica.) ¿Se puede concluir que las medias de los diámetros de las inclusiones son diferentes entre los dos gases de protección?

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
# 1 - α = 99%  
# α = 1%

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
x1 = 0.37

# %%
x2 = 0.40

# %% [markdown]
# $\overline{x}$<sub>1</sub> = 0.37  
# $\overline{x}$<sub>2</sub> = 0.40

# %% [markdown]
# #### Calculate ${s}$

# %%
s1 = 0.25

# %%
s2 = 0.26

# %% [markdown]
# ${ s }$<sub>1</sub> = 0.25  
# ${ s }$<sub>2</sub> = 0.26

# %% [markdown]
# #### Calculate ${n}$

# %%
n1 = 544

# %%
n2 = 581

# %% [markdown]
# ${ n }$<sub>1</sub> = 544  
# ${ n }$<sub>2</sub> = 581

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{0.37-0.40}{\sqrt{\frac{0.25^2}{544}+\frac{0.26^2}{581}}}$$

# %%
Zc = (x1-x2)/(math.sqrt((s1**2/n1)+(s2**2/n2)))
Zc

# %% [markdown]
# ${Zc}$ = -1.97

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# | Confidence | Significance | Left  | Right | Bilateral    |
# | ---------- | ------------ | ----  | ----- | ------------ |
# | 90%        | 10%          | -1.28 | 1.28  | ${\pm}$ 1.64 |
# | 95%        | 5%           | -1.64 | 1.64  | ${\pm}$ 1.96 |
# | 99%        | 1%           | -2.33 | 2.33  | ${\pm}$ 2.58 |

# %% [markdown]
# Z<sub>c</sub> = -1.97  
# Z<sub>0.01</sub> = ${\pm}$ 2.58

# %%
Z1 = 2.58
Z2 = -2.58

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
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 99% de confianza se puede concluir que las medias de los diámetros de las inclusiones son IGUALES entre los dos gases de protección
print('Con un 99% de confianza se puede concluir que las medias de los diámetros de las inclusiones son IGUALES entre los dos gases de protección')
