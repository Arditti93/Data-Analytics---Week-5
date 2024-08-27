import pandas as pd
import numpy as np 

# pd is short for pandas, we imported it as pd so when we want to use pandas we write pd 

# Notice .Series method uses a capital S
languages = pd.Series(["Python", "JavaScript", "Java", "SQL"])
# print(languages)

positions = pd.Series([3,1,2,4])
# print(positions)

df = pd.DataFrame({
    "Languages": languages,
    "Positions": positions
})
# print(df)

df = pd.DataFrame([("Anne", 30, "Dog"), ("Bill", 27, "Cat"), ("Steve", 55, "Rabbit")],
                   columns=["Name", "Age", "Fav Pet"])
# print(df)


df = pd.read_csv("speeds_1.csv")
# print(df)


df = pd.read_excel("speeds.xlsx")
print(df)


