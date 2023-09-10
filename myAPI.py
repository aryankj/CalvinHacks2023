# #from email import message
# #from turtle import title

# #import json
# import requests
# import random
# #gen = input("Enter the genre: ")
# moviesToID= {'Biography': '1', 
#              'Music': '10402', 
#              'Romance': '10749', 
#              'Family': '10751', 
#              'War': '10752', 
#              'News': '10763', 
#              'Reality': '10764', 
#              'Talk Show': '10767', 
#              'Adventure': '12', 
#              'Fantasy': '14', 
#              'Animation': '16', 
#              'Drama': '18', 
#              'Film Noir': '2', 
#              'Horror': '27', 
#              'Action': '28', 
#              'Game Show': '3', 
#              'Comedy': '35', 
#              'History': '36', 
#              'Western': '37', 
#              'Musical': '4', 
#              'Sport': '5', 
#              'Thriller': '53', 
#              'Short': '6', 
#              'Adult': '7', 
#              'Crime': '80', 
#              'Science Fiction': '878', 
#              'Mystery': '9648', 
#              'Documentary': '99'}

# url = "https://streaming-availability.p.rapidapi.com/v2/search/basic"

# headers = {
# 	"X-RapidAPI-Key": "7de7ab5477mshd7aeeeacf612a05p17ef09jsn5a180b4ccfd9",
# 	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
# }

# def getMovies(genre):
#     querystring = {
#                    "country":"us",
#                    "services":"netflix,prime.buy,hulu.addon.hbo,peacock.free",
#                    "output_language":"en",
#                    "show_type":"movie",
#                    "genre":genre,
#                    "show_original_language":"en", 
#                    "cursor" : "" 
#                    }
#     myMovies = []
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     jsonfile=response.json()
#     while jsonfile['hasMore']:
#         myList= jsonfile['result']
#         nextC = jsonfile['nextCursor']
#         for item in myList:
#             myMovies.append(item['title'])
#         querystring = {"country":"us","services":"netflix,prime.buy,hulu.addon.hbo,peacock.free",
#         "output_language":"en", "show_type":"movie","genre":"12","show_original_language":"en", "cursor" : nextC}
#         response = requests.request("GET", url, headers=headers, params=querystring)
#         jsonfile=response.json()
#     return myMovies

# def getRandomMovie(movies):
#     value = random.randint(0, len(movies)-1)
#     return movies[value]


# def updateTextFile(genre):
#     f1 = open(genre+'txt',"w")
#     for movie in getMovies(genre):
#         f1.write(movie+'\n')
#     f1.close()

# def getMoviesFromFile(filename):
#     f1= open(filename, "r")
#     return [movie for movie in f1 ]

# #updateTextFile(moviesToID['Adventure'])


# #movies = getMoviesFromFile('12.txt')
#import json
import requests
import random
moviesToID= {'Biography': '1',
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
             'Update':'Update'}

url = "https://streaming-availability.p.rapidapi.com/v2/search/basic"

headers = {
   "X-RapidAPI-Key": "7de7ab5477mshd7aeeeacf612a05p17ef09jsn5a180b4ccfd9",
   "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

def getMovies(genre):
    querystring = {
                   "country":"us",
                   "services":"netflix,prime.buy,hulu.addon.hbo,peacock.free",
                   "output_language":"en",
                   "show_type":"movie",
                   "genre":genre,
                   "show_original_language":"en",
                   "cursor" : ""
                   }
    myMovies = []
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonfile=response.json()
    while jsonfile['hasMore']:
        myList= jsonfile['result']
        nextC = jsonfile['nextCursor']
        for idx in range(len(myList)):
            #myMovies.append(myList[idx]['title'] + "**" + myList[idx]['overview'] + '\n')
            myMovies.append(myList[idx]['title'])
        querystring = {"country":"us","services":"netflix,prime.buy,hulu.addon.hbo,peacock.free",
        "output_language":"en", "show_type":"movie","genre":"12","show_original_language":"en", "cursor" : nextC}
        response = requests.request("GET", url, headers=headers, params=querystring)
        jsonfile=response.json()
    return myMovies

def getRandomMovie(movies):
    value = random.randint(0, len(movies)-1)
    return movies[value]



def updateTextFile(genre):
    f1 = open(genre+'.txt',"w")
    for movie in getMovies(genre):
        f1.write(movie+'\n')
    f1.close()

def getMoviesFromFile(filename):
    # if filename == "Update":
    #     updateTextFile(filename)
    # else:
    f1= open(filename+'.txt', "r")
    return [movie for movie in f1 ]
    f1.close()

#updateTextFile(moviesToID['Adventure'])


#movies = getMoviesFromFile('12.txt')

# querystring = {
#                    "country":"us",
#                    "services":"netflix,prime.buy,hulu.addon.hbo,peacock.free",
#                    "output_language":"en",
#                    "show_type":"movie",
#                    "genre":"1",
#                    "show_original_language":"en",
#                    "cursor" : ""
#                    }
# myMovies = []
# response = requests.request("GET", url, headers=headers, params=querystring)
# jsonfile=response.json()
#
# print(jsonfile['result'][0]['title'] + '\n' + jsonfile['result'][1]['overview'])
# print( [key for key in jsonfile['result'][0]['streamingInfo']['us']])


