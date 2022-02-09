# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 13

# %% [markdown]
# 13. Una alumna del Centro Universitario de Ciencias de la Salud imparte asesorías a alumnos de medicina de primer semestre en el ciclo A y en el ciclo B (Ciclo A: Inicio clases en Enero; Ciclo B: Inicio clases en Agosto). Después de 1 año de dar asesorías obtuvo los siguientes resultados de sus asesorados: Ciclo A promedio 91 con 37 alumnos y desviación de 2.1, Ciclo B con un promedio final de 83.7 con 61 alumnos y desviación de 2.5.
# Si se usa significancia del 0.05, ¿Se puede afirmar que el ciclo A tiene, por mucho, mejor rendimiento que los del ciclo B?

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ<sub>1</sub> ≤ µ<sub>2</sub>  
# H<sub>1</sub>: µ<sub>1</sub> > µ<sub>2</sub>

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
x1 = 91

# %%
x2 = 83.7

# %% [markdown]
# $\overline{x}$<sub>1</sub> = 91  
# $\overline{x}$<sub>2</sub> = 83.7

# %% [markdown]
# #### Calculate ${s}$

# %%
s1 = 2.1

# %%
s2 = 2.5

# %% [markdown]
# ${ s }$<sub>1</sub> = 2.1  
# ${ s }$<sub>2</sub> = 2.5

# %% [markdown]
# #### Calculate ${n}$

# %%
n1 = 37

# %%
n2 = 61

# %% [markdown]
# ${ n }$<sub>1</sub> = 37  
# ${ n }$<sub>2</sub> = 61

# %% [markdown]
# #### Calculate ${ Z }$

# %% [markdown]
# $$Z = \frac{91-83.7}{\sqrt{\frac{2.1^2}{37}+\frac{2.5^2}{61}}}$$

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
# Z<sub>0.05</sub> = 1.64

# %%
Z = 1.64

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
# Con un 95% de confianza se puede concluir que el ciclo A tiene, por mucho, mejor rendimiento que los del ciclo B.
print('Con un 95% de confianza se puede concluir que el ciclo A tiene, por mucho, mejor rendimiento que los del ciclo B.')
