# %%

import numpy as np
import pandas as pd
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

print(lista*2)
print(nplista*2)
print(pdlista*2)



# %%
df = pd.read_csv("insurance.csv")
print(df)

# %%
df.head()
#df.tail()
#df.sample()

# %%
#df.info()
df.describe()

# %%
df[['age','bmi']]

# %%
df[:2][['age','bmi']]

# %%
df[10:11]

# %%
