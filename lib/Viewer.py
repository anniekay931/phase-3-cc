class Viewer:

    def __init__(self, username):
        self._username = username
        self._reviews = []
        self.reviewed_movies = []
    
    @property
    def username(self):
        return self._username
    
    def set_username(self, new_username):
        if isinstance(new_username, str) and 6 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise ValueError("Username must be a unique string between 6 and 16 characters")
    
    @property
    def reviews(self):
        return self._reviews
    
    def reviewed_movies(self):
        return [review.movie() for review in self._reviews]
    
    def reviewed_movie(self, movie):
        return any(review.movie() == movie for review in self._reviews)
    
    def rate_movie(self, movie, rating):
        if self.reviewed_movie(movie):
            raise ValueError("Viewer has already reviewed this movie")
        review = Review(viewer=self,
        movie=movie, rating=rating)
        self._reviews.append(review)
