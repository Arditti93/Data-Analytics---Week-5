import pandas as pd
import numpy as np 

languages = pd.Series(["Python", "JavaScript", "Java", "SQL"])
positions = pd.Series([3,1,2,4])


df = pd.DataFrame({
    "Languages": languages,
    "Positions": positions
})

# print(df)
# print("-----------")
# Updating the orginal DataFrame with PHP in the languages column and 11 in the rankings column

df.loc[4] = ["PHP", 11] 
# print(df)

# print("-----------")
df.loc[3.5] = ["KESL", 20]
# Sorts DataFrame into index order even if we add a new row between 2 existing ones
df = df.sort_index() 
# print(df)
# print("-----------")
#  add a new column to the existing DataFrame with these values 
df["Rankings 2022"] = [4,1,2,3,10,15]
df["Rankings 2020"] = [5,10,45,20,7,8]
df["Rankings 2019"] = [8,9,3,4,3,7]
# Insert a column at a spefic index
df.insert(3, "Rankings 2021", [6,7,9,3,9,2])
# Update an exisiting column name to a new one without making a new data frame
df.rename(columns={"Positions" : "Rankings 2023"}, inplace=True)
# print(df)

# DAY 2 
# print a column from the DataFrame
# print(df["Rankings 2022"])
print(df)
# print one index from the DataFrame
# print(df.loc["SQL"])

# Change which column is the index of the DataFrame
df = df.set_index("Languages")

print(df.loc[:"Java", :"Rankings 2019":2])


