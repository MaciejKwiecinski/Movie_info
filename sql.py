create_table = """CREATE TABLE movie (
                  movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  movie_title TEXT,
                  movie_year TEXT,
                  movie_rated TEXT,
                  movie_released TEXT,
                  movie_runtime TEXT,
                  movie_genre TEXT,
                  movie_director TEXT,
                  movie_writer TEXT,
                  movie_actors TEXT,
                  movie_plot TEXT,
                  movie_language TEXT,
                  movie_country TEXT,
                  movie_awards TEXT,
                  movie_poster TEXT,
                  movie_ratings TEXT,
                  movie_metascore TEXT,
                  movie_imdbrating TEXT,
                  movie_imdbvotes TEXT,
                  movie_imdbid TEXT,
                  movie_type TEXT,
                  movie_dvd TEXT,
                  movie_boxoffic TEXT,,
                  movie_production TEXT,
                  movie_website TEXT,
                  movie_response TEXT);"""

insert_into = """INSERT INTO movie VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
                '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"""