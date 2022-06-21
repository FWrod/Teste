string="""SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53"""
dici={}
for e in string.split('\n'):
    estado=e.split('–')[0]
    faturamento=float(e.split('–')[1].replace('R$','').replace('.','').replace(',','.'))
    dici[estado]=faturamento

import pandas as pd

df=pd.Series(dici)

pcts=df.div(df.sum()).mul(100).astype(str).map(lambda x: x[:4]+'%')
print(" Os percentiais foram para cada estado \n{}".format(pcts))

