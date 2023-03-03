class Review:
    
    def __init__(self, viewer, movie, rating):
        self._viewer = None
        self._movie = None
        self._rating = None
        self.set_rating(rating)
        self.set_movie(movie)
        self.set_rating(rating)

    def rating(self):
        return self._rating
    
    def set_rating(self, new_rating):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise ValueError("Rating must be an integer between 1 and 5")

    def movie(self):
        return self._movie
    
    def set_movie(self, new_movie):
        if isinstance(new_movie, Movie):
            self._movie = new_movie
        else:
            raise ValueError("Movie must be a Movie instance")
    def rating(self):
        return self._rating
    
    def set_rating(self, new_rating):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise ValueError("Rating must be an integer between 1 and 5")
    
    def viewer(self):
        return self._viewer
