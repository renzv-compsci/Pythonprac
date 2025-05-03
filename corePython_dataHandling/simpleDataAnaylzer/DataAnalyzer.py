import pandas as pd
import matplotlib.pyplot as plt 

pracData = pd.read_csv('C:\\Users\\Renz\\Pythonprac\\corePython_dataHandling\\simpleDataAnaylzer\\PracDataSet - Sheet1.csv')

print(pracData.to_string()) # reads the csv file as string
print(pracData.isnull().sum()) # checks the csv file if it has missing data
print(pracData.describe()) # basic statistics of the csv data

average_rating = pracData ['Rating '].mean() # Calculates the average rating of the movie 
print(f"Average Rating: {average_rating}")

most_common_genre = pracData['Genre '].mode()[0] # Finds the most common movie genre based on the csv
print(f"Common Genre: {most_common_genre}")


# sets up the bar plot for visual data 
genre_counts = pracData['Genre '].value_counts()
genre_counts.plot(kind='bar')
plt.title('Genre Distribution')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

# sets up the bar plot for visual data 
rating_average = pracData['Rating '].value_counts()
pracData.sort_values(by = 'Rating ', ascending=False).head(5) # sorts the date and displays the top 5 movie with highest rating
rating_average.plot(kind='bar')
plt.title('Average Rating')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

# Filter genre
print (pracData[pracData['Genre '] == 'Action'])
genre_counts.sort_values(ascending=False).plot(kind='bar')

# save filtered CSV
action_genre = pracData[pracData['Genre '] == 'Action']
action_genre.to_csv("actionMovies.csv", index=False)