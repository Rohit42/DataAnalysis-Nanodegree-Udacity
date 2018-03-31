import pandas as pd

def truncate_names(string):
	comma_pos = string.find(",")
	string =  string[:comma_pos]
	return string.rsplit(' ', 1)[0].lower()

def truncate_full(string):
	string = str(string)
	comma_pos = string.find(",")
	if(comma_pos == -1):
		return string.lower()
	return string[:comma_pos].lower()

names_df = pd.read_csv("PEP_2016_PEPANNRES.csv")
names_df["Names"] = names_df["Names"].apply(truncate_names)

full_df = pd.read_csv("P00000001-TX.csv")
full_df["Names"] = full_df["contbr_city"].apply(truncate_full)

gender_df = pd.read_csv("canidates.csv")

finished_df = pd.merge(full_df,names_df,how = "left", on=["Names"])
finished_df = pd.merge(finished_df,gender_df,how = "left", on=["cand_nm"])

finished_df.to_csv("New Dataset.csv")


