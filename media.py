"""media.py: stores movie data."""
__author__ = "Hrafnhildur Jonasdottir"


class Movie():
    """
    This class stores movie data such as a movie title,
    a poster url and a trailer url
    """
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
