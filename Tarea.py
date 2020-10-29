import pandas as pd
 
df = pd.read_csv('ulabox.csv')
 
# df.info()
del df['order']
# print("Tamaño del dataset:",df.shape)
# parte 2
print(df)
print("\nTIPO DE VARIABLE:\nCustumer = continuo\nTotal = continuo\nDiscount = discreto\nWeekDay = ordinal\nHour = discreto\nFood = discreto\nFresh = discreto\nDrinks = discreto\nHome = discreto\nBeauty = discreto\nHealth = discreto\nBaby = discreto\nPets = discreto\n")
# parte 3
print("----------------Minimo-----------------")
print(df.min())
print("----------------Maximo-----------------")
print(df.max())
# parte 4

print("----------------Medias-----------------")
print(df.mean())
print("\n----------------Medianas-----------------")
print(df.median())
print("\n----------------Moda-----------------")
print(df.mode())
print("\n----------------Desviacion estandar-----------------")
print(df.std())
print("\n----------------Cuartiles-----------------")
print(df.quantile([.25, .5, .75]))

#Conclusiones
# Pues gracias al ver la infromacion de cada variable podemos saber su comportamiento segun los datos dados 
# pero en caso de food en adelante no se entiende muy bien la informacion dada desde el principio ya que en algunas cosas en vez de poner un numero exacto pone un porcentaje
# print(df.describe())
