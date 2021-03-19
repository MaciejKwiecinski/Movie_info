from functions import add_to_list, next_move
from MovieBase import MovieBase
import os

arr = []
inp = input("Enter the title of the video : ")

while inp.lower() != "finish entering the titles":
    if type(inp) == list:
        for title in inp:
            add_to_list(inp, arr)
    if type(inp) == str:
        add_to_list(inp, arr)
    inp = input()

if arr != []:
    movies = MovieBase(arr)
else:
    print("No movie list here")
    exit(-2)

move = input("What next? ")

while move.lower() != "end":
    next_move(move.lower(), movies)
    move = input("What next? ")
    os.system('cls||clear')

exit(0)