from viewer import Viewer
from movie import Movie

class Review:
    def __init__(self, rating, viewer, movie):
        self.movie = movie
        self.viewer = viewer
        self.rating = rating

        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5, inclusive.")
        if not isinstance(self.viewer, Viewer):
            raise TypeError("Viewer must be an instance of the Viewer class.")
        if not isinstance(self.movie, Movie):
            raise TypeError("Movie must be an instance of the Movie class.")

    def get_rating(self):
        return self._rating

    def set_rating(self, new_rating):
        if new_rating < 1 or new_rating > 5:
            raise ValueError("Rating must be between 1 and 5, inclusive")
        self._rating = new_rating

    def get_viewer(self):
        return self._viewer

    def set_viewer(self, new_viewer):
        if not isinstance(new_viewer, Viewer):
            raise TypeError("Viewer must be an instance of Viewer class")
        self._viewer = new_viewer

    def get_movie(self):
        return self._movie

    def set_movie(self, new_movie):
        if not isinstance(new_movie, Movie):
            raise TypeError("Movie must be an instance of Movie class")
        self._movie = new_movie
        new_movie.reviews.append(self)




