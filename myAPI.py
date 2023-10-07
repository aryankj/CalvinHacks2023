import requests
import random

# Mapping of movie genres to their corresponding IDs
moviesToID = {
    'Biography': '1',
    'Music': '10402',
    'Romance': '10749',
    'Family': '10751',
    'War': '10752',
    'News': '10763',
    'Reality': '10764',
    'Talk Show': '10767',
    'Adventure': '12',
    'Fantasy': '14',
    'Animation': '16',
    'Drama': '18',
    'Film Noir': '2',
    'Horror': '27',
    'Action': '28',
    'Game Show': '3',
    'Comedy': '35',
    'History': '36',
    'Western': '37',
    'Musical': '4',
    'Sport': '5',
    'Thriller': '53',
    'Short': '6',
    'Adult': '7',
    'Crime': '80',
    'Science Fiction': '878',
    'Mystery': '9648',
    'Documentary': '99',
    'Update': 'Update'
}

url = "https://streaming-availability.p.rapidapi.com/v2/search/basic"

headers = {
   "X-RapidAPI-Key": "7de7ab5477mshd7aeeeacf612a05p17ef09jsn5a180b4ccfd9",
   "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

def get_movies(genre):
    querystring = {
        "country": "us",
        "services": "netflix,prime.buy,hulu.addon.hbo,peacock.free",
        "output_language": "en",
        "show_type": "movie",
        "genre": genre,
        "show_original_language": "en",
        "cursor": ""
    }
    my_movies = []
    
    while True:
        response = requests.get(url, headers=headers, params=querystring)
        jsonfile = response.json()
        my_list = jsonfile['result']
        
        for movie in my_list:
            my_movies.append(movie['title'])
        
        if not jsonfile['hasMore']:
            break
        
        querystring["cursor"] = jsonfile['nextCursor']
    
    return my_movies

def get_random_movie(movies):
    return random.choice(movies)

def update_text_file(genre):
    movies = get_movies(genre)
    
    with open(f"{genre}.txt", "w") as f:
        for movie in movies:
            f.write(movie + '\n')

def get_movies_from_file(filename):
    with open(f"{filename}.txt", "r") as f:
        return [line.strip() for line in f]

# Example usage:
# update_text_file(moviesToID['Adventure'])
# movies = get_movies_from_file('Adventure')
# random_movie = get_random_movie(movies)
# print(random_movie)
