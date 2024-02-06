movies = [
    {"title": "Avengers the Endgame", "genre": "sci fi", "rating": 8.7, "year": 1999},
    {"title": "Squid Game", "genre": "crime", "rating": 9.2, "year": 1972},
    {"title": "The K.G.F Chapter 2", "genre": "action", "rating": 8.0, "year": 2012},
    {"title": "The Notebook", "genre": "romance", "rating": 7.8, "year": 2004},
    {"title": "The Lion King", "genre": "animation", "rating": 8.5, "year": 1994}
]
user_genre = str(input('Enter Genre; '))
user_rating = eval(input('Enter Rating; '))
user_year = int(input('Enter Year of Movie Release; '))
def recommend_movies(movies, genre, rating, year):
    recommended_movies = []
    for movie in movies:
        if movie["genre"] == user_genre and movie["rating"] >= user_rating and movie["year"] >= user_year:
            recommended_movies.append(movie["title"])
    return recommended_movies
recommended_movies = recommend_movies(movies, user_genre, user_rating, user_year)
for movie in recommended_movies:
    print(movie)
    print()
print("Recommended movies for you based on your preferences")