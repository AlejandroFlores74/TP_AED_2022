class Series:
    def __init__(self, poster_link, series_title, runtime_of_series, certificate, runtime_of_episodes,
                 genre, imdb_rating, overwiew, star1, star2, star3, star4, no_of_vote):
        self.poster_link = poster_link
        self.series_title = series_title
        self.runtime_of_series = runtime_of_series
        self.certificate = certificate
        self.runtime_of_episodes = runtime_of_episodes
        self.genre = genre
        self.imdb_rating = imdb_rating
        self.overwiew = overwiew
        self.star1 = star1
        self.star2 = star2
        self.star3 = star3
        self.star4 = star4
        self.no_of_vote = no_of_vote

    def __str__(self):
        cadena = '\nPoster_Link: ' + self.poster_link + '\n'
        cadena += 'Series_Title: ' + self.series_title + '\n'
        cadena += 'Runtime_of_Series: ' + self.runtime_of_series + '\n'
        cadena += 'Certificate: ' + self.certificate + '\n'
        cadena += 'Runtime_of_Episodes: ' + self.runtime_of_episodes + '\n'
        cadena += 'Genre: ' + self.genre + '\n'
        cadena += 'IMDB_Rating: ' + self.imdb_rating + '\n'
        cadena += 'Overwiew: ' + self.overwiew + '\n'
        cadena += 'star1: ' + self.star1 + '\n'
        cadena += 'Star2: ' + self.star2 + '\n'
        cadena += 'star3: ' + self.star3 + '\n'
        cadena += 'Star4: ' + self.star4 + '\n'
        cadena += 'No_of_Vote: ' + self.no_of_vote + '\n'
        return cadena
