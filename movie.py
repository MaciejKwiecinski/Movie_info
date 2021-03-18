class Movie:
    def __init__(self, jsonObj):
        self.jsonObj = jsonObj
        self.title = self.jsonObj['Title']
        self.rottentomato = self.set_rottentomato()
        self.metascore = self.set_metascore()
        self.imdbRating = self.set_imdbRating()
        self.imdbVotes = self.jsonObj['imdbVotes']
        self.boxOffice = self.set_boxOffice()

    def set_rottentomato(self):
        try:
            if self.jsonObj['Ratings'][1]['Source'] == "Rotten Tomatoes" and \
                    self.jsonObj['Ratings'][1]['Value'][:-1].isdigit():
                return float(self.jsonObj['Ratings'][1]['Value'][:-1])
            else:
                return False
        except IndexError:
            return False

    def set_metascore(self):
        try:
            if self.jsonObj["Metascore"].isdigit():
                return float(self.jsonObj["Metascore"])
            else:
                return False
        except IndexError:
            return False

    def set_imdbRating(self):
        try:
            if self.jsonObj['imdbRating'].isdigit():
                return float(self.jsonObj['imdbRating'])
            else:
                return False
        except IndexError:
            return False

    def set_boxOffice(self):
        try:
            if self.jsonObj['BoxOffice'][1:].replace(",", "").isdigit():
                return int(self.jsonObj['BoxOffice'][1:].replace(",", ""))
            else:
                return False
        except Exception:
            return False

    def create_row(self):
        s = [v for k,v in self.jsonObj.items()]
        return s

    def create_first_row(self):
        s = [k for k in self.jsonObj]
        return s