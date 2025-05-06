import pandas as pd 
import matplotlib.pyplot as mp
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

# FILTERING 

# Movies with rating above 8.0 
filteredby_Rating = movieData[movieData['Rate'] > 8.0][['Title', 'Rate']]
print(f"Movies with rating above 8.0: \n{filteredby_Rating}")

# Movies with metascore of above 80 
filteredby_Metascore = movieData[movieData['Metascore'] > 85][['Title', 'Metascore']]
print(f"Movies with metascore above 80: \n{filteredby_Metascore}")

# Top 5 most highest metascore
top5_Metascore = movieData[movieData['Metascore'] > 90][['Title', 'Rate', 'Metascore']]
sortedby_Metascore = top5_Metascore.sort_values(by='Metascore', ascending=False).head(5)
print(f'Top 5 highest metascore: \n{sortedby_Metascore}')

# VISUALIZATION

# Average rating per genre (Bar Chart)
mp.figure() # seperate tables
ave_rating = movieData.groupby('Genre')['Rate'].mean()
ave_rating.plot(kind='bar')
mp.title('Average rating by genre')
mp.xlabel('Genre')
mp.ylabel('Rating')
mp.tight_layout()
mp.show()
print(f'Average rating per genre: {ave_rating}')

# Average rating per certificate (Line plot)
mp.figure() # seperate tables
aveRating_perCertificate = movieData.groupby('Certificate')['Rate'].mean()
aveRating_perCertificate.plot(kind='line')
mp.title('Average rating per certificate')
mp.xlabel('Certificate')
mp.ylabel('Rating')
mp.tight_layout()
mp.show()
print(f'Average rating per certificate: {aveRating_perCertificate}')