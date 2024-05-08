import pandas as pd

df=pd.read_csv('testing.csv')

data=[]

df=df.drop(columns=['Photo', 'Carat', 'Cert','Stone ID', 'Base Off %'])
data=df.columns.tolist()
# data.append(df['Flour'].tolist())
# data.append(df['Cut'].tolist())


# d=[]
# for i in range(len(data[0])):
#     l=[]
#     for j in range(2):
#             l.append(data[j][i])
#     d.append(l)
print(data)