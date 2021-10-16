import pandas as pd
df = pd.DataFrame({
    'name':
    ['orange','banana','lemon','mango','apple'],
    'price':
    [2,3,7,21,11],
    'stock':
    ['Yes','No','Yes','No','Yes']
})
print(df.iloc[0]['price'])
print(df.iloc[2]['stock'])

print(df.iat[0,1])
print(df.at[1,'name'])

# python 3.x
import pandas as pd
df = pd.DataFrame({
    'name':
    ['orange','banana','lemon','mango','apple'],
    'price':
    [2,3,7,21,11],
    'stock':
    ['Yes','No','Yes','No','Yes']
})
print(df['name'].values[2])


#pegar valores unicos de uma coluna
import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[7,1,5,4,2,1,4,4,8],'B':[1,2,8,5,3,4,2,6,8]})

print(df['A'].unique())
print(type(df['A'].unique()))