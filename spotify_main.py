import polars as pl
import matplotlib.pyplot as plt

  
# read the CSV file 
df = pl.read_csv('spotify_2023.csv', ignore_errors=True)


def spotify_song():
    return df

# check the head
# df.head()

# compute summary statistics
summary = df.describe()
print(summary)

track_col = ['streams','bpm', 'key', 'mode', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']
df_voi = df[track_col]
df_voi.head()

summary_col = df_voi.describe()
print(summary_col)

# Sort the DataFrame by 'popularity' in descending order
df = pl.read_csv('spotify_2023.csv', ignore_errors=True)

# Sort the DataFrame by 'popularity' in descending order
df_sorted = df.sort("streams")

# Select the top 10 songs
top_songs = df_sorted.tail(10)
print(top_songs)

plt.figure(figsize=(12, 6))
plt.barh(top_songs['track_name'], top_songs['streams'], color='skyblue')
plt.xlabel('Popularity')
plt.ylabel('Track Name')
plt.title('Top 10 Songs with the Highest Popularity on Spotify')
plt.gca().invert_yaxis()  # Invert the y-axis to display the most popular song at the top
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.show()
