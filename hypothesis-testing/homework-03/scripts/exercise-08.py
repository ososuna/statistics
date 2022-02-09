# %% [markdown]
# # Hyphotesis test

# %% [markdown]
# ## Exercise 8

# %% [markdown]
# 8. Se desea contrastar con un nivel de significancia del 5% la hipótesis de que la talla media de los hombres de 18 o más años de un país es igual o mayor a 175. Suponiendo que la desviación típica de las tallas en la población vale 4, contraste dicha hipótesis frente a la alternativa de que es menor, con una muestra de n = 15 hombres seleccionados al azar, cuyas alturas son las del ejercicio anterior.
# 167 167 168 168 168 169 171 172 173 175 175 175 177 182 195

# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# %% [markdown]
# ### 1. Define the null and alternate hypotheses

# %% [markdown]
# H<sub>0</sub>: µ ≥ 175  
# H<sub>1</sub>: µ < 175

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
data = [167, 167, 168, 168, 168, 169, 171, 172, 173, 175, 175, 175, 177, 182, 195]

# %%
x = sum(data) / len(data)
x

# %% [markdown]
# $\overline{x}$ = 173.46

# %% [markdown]
# #### Calculate ${µ}$

# %%
mu = 175
mu

# %% [markdown]
# ${µ}$ = 175

# %% [markdown]
# #### Calculate ${s}$

# %%
s = 4
s

# %% [markdown]
# ${ s }$ = 4

# %% [markdown]
# #### Calculate ${n}$

# %%
n = 15

# %% [markdown]
# ${ n }$ = 15

# %% [markdown]
# #### Calculate ${ t }$

# %% [markdown]
# $$t = \frac{173.46-175}{\frac{4}{ \sqrt{15}}}$$

# %%
tc = (x-mu)/(s/math.sqrt(n))
tc

# %% [markdown]
# ${t}$ = -1.48

# %% [markdown]
# ### 5. Set decision rule

# %% [markdown]
# t<sub>c</sub> = -1.48  
# t<sub>0.05</sub> = -1.76

# %%
t = -1.76

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
plt.legend(["tc", "t0.05", "µ"])
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# %% [markdown]
# #### H<sub>0</sub> is accepted
# #### H<sub>1</sub> is rejected

# %% [markdown]
# ### 7. Draw conclusions

# %% [markdown]
# Con un 95% de confianza se puede concluir que la talla media de los hombres de 18 o más años de un país es igual a 175.
print('Con un 95% de confianza se puede concluir que la talla media de los hombres de 18 o más años de un país es igual a 175.')
