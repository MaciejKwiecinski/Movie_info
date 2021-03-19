from movie import Movie
import urllib.request
import json


def is_existing(title, key="e9b8446e"):
    title = title.strip().replace(" ", "+")
    url = "http://www.omdbapi.com/?apikey=" + key + "&t=" + title
    data = json.load(urllib.request.urlopen(url))
    if data["Response"] == "True":
        return Movie(data)
    else:
        print("There is no movie with title like " + title)
        return -1

def add_to_list(title, arr):
    var = is_existing(title)
    if var != -1:
        arr.append(var)

def next_move(move, m1):
    if move == "highest-grossing":
        m1.highest_box_office()
    elif move == "best rated imdb":
        m1.highest_imdb_rating()
    elif move == "list of titles":
        m1.print_titles()
    elif move == "average rating":
        m1.average_rating()
    elif move == "to json":
        name = input("Name new file: ")
        m1.generate_json(name)
    elif move == "to csv":
        name = input("Name new file: ")
        m1.generate_csv(name)
    # elif move == "to db":
    #     name = input("Name new file: ")
    #     m1.generate_db(name)