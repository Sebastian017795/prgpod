#%%
import pandas as pd

df = pd.read_csv("ulabox.csv")
del df['order']
df.head()


# %%
df.describe()

# %%
import seaborn as sns

sns.set_theme(style="white")

# %%
df['total_it'] = pd.cut(df.total_items, [1,15,30,45,300], labels=['Comprador muy bajo', 'comprador bajo', 'Comprador medio', 'Comprador alto'])
df.head(10)
#sns.displot(data=df , x="customer",y="total_it" )

# %%
sns.scatterplot(data=df , x="customer",y="discount%", hue="total_it" )

# %%
