import pandas as pd

df2 = pd.read_csv("New Dataset.csv")

print(df2[df2["Population"] > 500000].nunique())