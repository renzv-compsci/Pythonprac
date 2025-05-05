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

# Highest movie metascore
max_movieMetaScore = movieData['Metascore'].max()
print(f"Highest Movie Metascore: {max_movieMetaScore}")

# DATA GROUPING 

# Data Spliting and Explode (Average rating per genre)
movieData['Genre'] = movieData['Genre'].str.split(', ')
movieData = movieData.explode('Genre') 

# Average rating per genre
ave_ratingGenre = movieData.groupby('Genre')['Rate'].mean()
print(f"Average Rating per Genre: {ave_ratingGenre}")

# Highest movie metascore per genre
max_genreMetaScore = movieData.groupby('Genre')['Metascore'].max()
print(f"\nHighest metascore per genre: {max_genreMetaScore}")

# Data Splitting and Explode (Average rating per certificate)
movieData['Certificate'] = movieData['Certificate'].str.split(', ')
movieData = movieData.explode('Certificate')

# Average rating per certificate
ave_rateperYear = movieData.groupby('Certificate')['Rate'].mean()
print(f"\nAverage rating per certifacate: {ave_rateperYear}")
