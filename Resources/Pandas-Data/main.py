import pandas as pd

# Load the pokemon csv
df = pd.read_csv('pokemon_data.csv')

# Lists the first 3 names and hp
#print(df[["Name", "HP"]].head(3))

# Lists 3 rows in between 1 and 4
#print(df.iloc[1:4])

# Prints the elemet on row 2 col 1
#print(df.iloc[2,1])

# Iterates through a list to show col values one at a time
#for index, row in df.iterrows():
#   print(index, row)

# Metrics of the data
#print(df.describe())

# Sorts data by Type aplabetically then sorts by HP
#print(df.sort_values(["Type 1", "HP"], ascending=[1, 0]))

# Creating a new column. May not save properly
#df["Total"] = df["HP"] + df["Attack"] + df["Defense"] # + ...
#print(df.head(5))

# Deleting a column
#df = df.drop(columns=["Total"])
#print(df.head(5))

# Saving a csv without the additional index, separated with tab intent
df.to_csv("modified_csv", index=False, sep='\t')