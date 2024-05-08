import pandas as pd

df = pd.read_csv("C:\\Users\\Prince\\Desktop\\My-API\\testing.csv")
df=df.fillna(0)

def show(col):
     global df
     error=""
     columns=df.columns.tolist()
     data=[]
     cols=[]
     for c in col:
          if c in columns:
               cols.append(c)
               data.append(df[c].tolist())
          else:
               error=f"{c} column name is not present.\n"
               return cols,data,error
     d=[]
     for i in range(len(data[0])):
          l=[]
          for j in range(len(cols)):
                 l.append(data[j][i])
          d.append(l)
     # print(d)
     return cols,d,error

def hide(col):
     global df
     df1=df
     columns=df.columns.tolist()
     data=[]
     error=""
     for c in col:
          if c in columns:
               df1=df1.drop(columns=[c])
          else:
               error=f"{c} column name is not present."
               return columns,data,error
     df=df1
     columns=df.columns.tolist()
     data=df.values.tolist()
     return columns,data,error

def query(response):
    global df
    columns=df.columns.tolist()
    data=[]
    error=""
    if response[1] is None:
         error="Give appropriate inputs."
    elif response[0].lower()=="show":
         col=response[1]
         columns, data,error=show(col)
    elif response[0].lower()=="hide":
         col=response[1]
         columns, data,error=hide(col)
    else:
         error="Give appropriate inputs."
    return columns,data,error