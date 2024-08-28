import pandas as pd

df = pd.read_csv("results.csv")
print(df.info())

print(df.describe())

df = pd.read_csv("spotify_songs.csv")
print(df)

# will tell us the size of the dataset in rows and column s
print(df.shape)

# will tell us the names of the columns used in the data
print(df.columns)

# will give us a snapshot of the begining of the frame
print(df.head())

print(df["playlist_genre"].value_counts())
print("-----------")
print(df["playlist_genre"].mode())
print("-----------")
print(df["playlist_genre"].mode()[0])

print(df["duration_ms"].median())
print(df["duration_ms"].mean())

max_ms = df["duration_ms"].max()
min_ms = df["duration_ms"].min()
print(max_ms - min_ms)

print(df["duration_ms"].sum())

# sort dataframe by values in a column
print(df.sort_values(by=["duration_ms"]))

print(df.groupby("playlist_genre")["duration_ms"].min())










