import unittest
import movie

class TestMovieClass(unittest.TestCase):
    def test_movie_title(self):
        result = movie.Movie("Avengers")
        self.assertEqual(result.title, "Avengers")


if __name__ == '__main__':
    unittest.main()