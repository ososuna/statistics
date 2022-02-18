# %% [markdown]
# # Regresión lineal

# %% [markdown]
# ## Mínimos cuadrados

# %%
import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.api as sm

# %% [markdown]
# ### 1. Tabla de mínimos cuadrados

# %%
x = [30, 28, 32, 25, 25, 25, 22, 24, 35, 40]
y = [25, 30, 27, 40, 42, 40, 50, 45, 30, 25]
X = sm.add_constant(x)

# %%
xy = []
xx = []
for i in range(len(x)):
  xy.append(x[i]*y[i])
  xx.append(x[i]*x[i])

# %%
ls_table = [[x], [y], [xy], [xx]]
ls_table

# %%
model = sm.OLS(y,X)
results = model.fit()
results.summary()

# %% [markdown]
# ### 2. Coeficiente de Pearson

# %%
pearson = np.corrcoef(x, y)[0][1]
pearson

# %% [markdown]
# ### 3. Coeficiente de determinación

# %%
coef = results.params[1]
coef

# %% [markdown]
# ### 4. Pendiente de la tangente

# %%
def slope(x1,y1,x2,y2):
    x = (y2 - y1) / (x2 - x1)
    return x

# %%
slope(x[0], y[0], x[2], y[2])

# %% [markdown]
# ### 5. Ordenada al origen

# %%
intercept = results.params[0]
intercept

# %% [markdown]
# ### 6. Establece la recta de regresión

# %%
ec = f"y = {coef} x + {intercept}"
ec

# %% [markdown]
# ### 7. Dibuja la gráfica de dispersión

# %%
plt.scatter(x, y); plt.xlabel('Producción de trigo'); plt.ylabel('Precio de la harina');

# %% [markdown]
# ### 8. Línea de tendencia

# %%
y_pred = results.predict(X)

# %%
plt.scatter(x, y); plt.xlabel('Producción de trigo'); plt.ylabel('Precio de la harina');
plt.plot(x, y_pred, c='red', linewidth=2)
plt.text(23,10,ec)
plt.show()

# %% [markdown]
# ### 9. Conclusión

# %% [markdown]
# Entre menor es la producción de trigo mayor el precio de la harina, por lo tanto se espera que cuando suba el precio es porque sube la producción, el modelo tiene eficacia del 70% (r cuadrada).
print("Entre menor es la producción de trigo mayor el precio de la harina, por lo tanto se espera que cuando suba el precio es porque sube la producción, el modelo tiene eficacia del 70% (r cuadrada).")
