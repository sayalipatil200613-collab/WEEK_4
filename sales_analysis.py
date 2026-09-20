import pandas as pd
df=pd.read_csv("Sales_Data.csv")

print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

