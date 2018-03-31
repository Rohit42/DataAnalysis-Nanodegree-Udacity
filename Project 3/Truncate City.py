import pandas as pd

def truncate(string):
	comma_pos = string.find(",")
	string =  string[:comma_pos]
	return string.rsplit(' ', 1)[0]

names_df = pd.read_csv("PEP_2016_PEPANNRES.csv")
names_df["Names"] = names_df["Names"].apply(truncate)
print(names_df.head())


