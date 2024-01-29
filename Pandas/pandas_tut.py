import pandas as pd

df = pd.read_csv("./services.csv")

print(df)

print(df.columns)

print(df['id'])

print(max(df['id']))

