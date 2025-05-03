import pandas as pd 

movieData = pd.read_csv('C:\\Users\\Renz\\Pythonprac\\corePython_dataHandling\\simpleDataAnaylzer\\IMDB top 1000.csv')

# BASIC STATISTICS

# Average Movie Rating 
avg_movieCateg = movieData['Rate'].mean()
print(f"Average Movie Rating: {avg_movieCateg}")

# Highest and Lowest Rated Movies
min_rateMovie = movieData['Rate'].min()
print(f"Lowest Rated Movie: {min_rateMovie}")

max_rateMovie = movieData['Rate'].max()
print(f"Highest Rated Movie: {max_rateMovie}")

# Highest moview metascore
max_movieMetaScore = movieData['Metascore'].max()
print(f"Highest Movie Metascore: {max_movieMetaScore}")