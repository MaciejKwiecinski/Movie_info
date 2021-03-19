import unittest
from movie import *
from functions import *
from MovieBase import *

class TestMovieClass(unittest.TestCase):
    movie = is_existing("Avengers")
    arr = [is_existing("Avengers Endgame"), is_existing("The Big Bang Theory"), is_existing("Friends")]
    movies = MovieBase(arr)

    def test_functions(self):
        self.assertIsInstance(is_existing("Avengers"), Movie)
        self.assertEqual(-1, is_existing(""))

    def test_Movie(self):
        #variable test
        self.assertEqual(self.movie.title, "The Avengers")
        self.assertEqual(self.movie.imdbRating, 8.0)
        self.assertEqual(self.movie.boxOffice, 623357910)
        self.assertEqual(self.movie.metascore, 69.0)
        self.assertEqual(self.movie.rottentomato, 91.0)
        #method test
        self.assertEqual(self.movie.set_imdbRating(), 8.0)
        self.assertEqual(self.movie.set_boxOffice(), 623357910)
        self.assertEqual(self.movie.set_metascore(), 69.0)
        self.assertEqual(self.movie.set_rottentomato(), 91.0)
        self.assertEqual(self.movie.create_first_row(), ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Ratings', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production', 'Website', 'Response'])
        self.assertEqual(self.movie.create_row(), ['The Avengers', '2012', 'PG-13', '04 May 2012', '143 min', 'Action, Adventure, Sci-Fi', 'Joss Whedon', 'Joss Whedon (screenplay), Zak Penn (story), Joss Whedon (story)', 'Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth', "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.", 'English, Russian, Hindi', 'USA', 'Nominated for 1 Oscar. Another 38 wins & 79 nominations.', 'https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg', [{'Source': 'Internet Movie Database', 'Value': '8.0/10'}, {'Source': 'Rotten Tomatoes', 'Value': '91%'}, {'Source': 'Metacritic', 'Value': '69/100'}], '69', '8.0', '1,268,647', 'tt0848228', 'movie', '22 Nov 2015', '$623,357,910', 'Marvel Studios', 'N/A', 'True'])

    def test_MovieBase(self):
        #variable test
        self.assertEqual(self.movies.arr, self.arr)
        self.assertIsInstance(self.movies.arr[0], Movie)





if __name__ == '__main__':
    unittest.main()