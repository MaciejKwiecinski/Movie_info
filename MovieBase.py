import json
import csv

class MovieBase:
    def __init__(self, obj_array):
        self.arr = obj_array

    def print_titles(self):
        for movie in self.arr:
            print(movie.title)

    def highest_imdb_rating(self):
        x = self.arr[0]
        for movie in self.arr:
            if movie.imdbRating >= x.imdbRating:
                x = movie
        print("Najwyżej oceniany film w serwisie IMDB: " + x.title)

    def highest_box_office(self):
        x = self.arr[0]
        for movie in self.arr:
            if movie.boxOffice >= x.boxOffice:
                x = movie
        print("Film z największym Box Officem to: " + x.title)

    def metacritic_rating(self):
        mc = 0
        mcr = 0.0
        try:
            for movie in self.arr:
                if movie.metascore:
                    mcr+=movie.metascore
                    mc += 1
            print("1) Metacritic: " + str(mcr/mc) + "/100")
        except ZeroDivisionError:
            print("Brak ocen Metacritic")

    def rottentomato_rating(self):
        rt = 0
        rtr = 0.0
        try:
            for movie in self.arr:
                if movie.rottentomato:
                    rtr+=movie.rottentomato
                    rt += 1
            print("3) Rotten Tomato: " + str(rtr/rt) + "%")
        except ZeroDivisionError:
            print("Brak ocen Rotten Tomato")

    def imdb_rating(self):
        imdb = 0
        imdbr = 0.0
        try:
            for movie in self.arr:
                if movie.imdbRating:
                    imdbr+=movie.imdbRating
                    imdb += 1
            print("2) IMDB: " + str(imdbr/imdb) + "/10")
        except ZeroDivisionError:
            print("Brak ocen IMDB")

    def average_rating(self):
        print("Średnia ocena zapisanych filmów na: ")
        self.metacritic_rating()
        self.imdb_rating()
        self.rottentomato_rating()

    def generate_json(self, name):
        data = {}
        data['movie'] = []
        for movie in self.arr:
            data['movie'].append(movie.jsonObj)
        with open(name + '.txt', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()

    def generate_csv(self, name):
        with open(name + '.csv', 'w') as f:
            wr = csv.writer(f)
            wr.writerow(self.arr[0].create_first_row())
            for movie in self.arr:
                wr.writerow(movie.create_row())
        f.close()