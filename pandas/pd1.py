import pandas as pd
import matplotlib.pyplot as plt
#create a dataframe
df = pd.DataFrame({'name':['ones','yvonne'],'age':[12,34],'RegNo':['p101','B109'],'marks':[100,300]})
df.plot()
print(df.head(3))
print("-"*100)
print(df['age'].max())
print("-"*100)
print(df)
print("-"*100)
print(df.describe())
print("-"*100)
print(df.dtypes)
print("-"*100)
print(df.info())
print("-"*100)

expresion = lambda X:X**12
print(expresion(df['marks'].max()))
print("-"*100)
print(df.shape)
print("-"*100)
df1=pd.DataFrame({"temperature":[10,20,30,40,50,60,70],"time":[70,60,50,40,30,20,10]})
print("-"*100)
print(df1)
print("-"*100)
print(df1.plot.scatter(x="temperature", y="time",alpha=0.5))
