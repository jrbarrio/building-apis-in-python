# Loop through the dictionary
genre_sales = {'Adventure': 367500000, 'Horror': 312500000, 'Literature': 80000000, 'Manga': 5166000000, 'Mystery': 300000000, 'Romance': 252500000, 'Thriller': 320000000}

for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)