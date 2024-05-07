import pandas as pd

df = pd.read_csv("C:\\Users\\Prince\\Desktop\\My-API\\testing.csv")
df=df.fillna(0)

def show(col):
     global df
     error=""
     columns=df.columns.tolist()
     data=[]
     if col in columns:
          columns= col
          data=df[col].tolist()
     else:
          error="Entered column name is not present."
     return columns,data,error

def hide(col):
     global df
     columns=df.columns.tolist()
     data=[]
     error=""
     if col in columns:
          df=df.drop(columns=[col])
          columns=df.columns.tolist()
          data=df.values.tolist()
     else:
          error="Entered column name is not present."
     return columns,data,error

def query(response):
    global df
    columns=df.columns.tolist()
    data=[]
    error=""
    if response[0].lower()=="show":
         col=response[1]
         columns, data,error=show(col)
    elif response[0].lower()=="hide":
         col=response[1]
         columns, data,error=hide(col)
    else:
         error="Give appropriate inputs."
    return columns,data,error