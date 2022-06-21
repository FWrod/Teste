import pandas as pd

df=pd.read_json('dados.json').set_index('dia')
# Mínimo
print('O menor valor no mês é {}'.format(df.min().values[0]))

#Máximo
print('O maior valor no mês é {}'.format(df.max().values[0]))

# Média dos não nulos
média=df[df.squeeze()!=0].mean().values[0]
print('O maior valor no mês é {}'.format(média))
