from functions import add_to_list, next_move
from MovieBase import MovieBase
import os

arr = []
key = input("Podaj swój API key do OMDB: ")
inp = input("Podawaj tytuły filmów: ")

while inp != "end":
    if type(inp) == list:
        for title in inp:
            add_to_list(inp, arr)
    if type(inp) == str:
        add_to_list(inp, arr)
    inp = input()

if arr != []:
    movies = MovieBase(arr)
else:
    print("Brak listy filmów")
    exit(-2)

move = input("Co robimy? ")

while move.lower() != "end":
    next_move(move.lower(), movies)
    move = input("Co robimy? ")
    os.system('cls||clear')

exit(0)