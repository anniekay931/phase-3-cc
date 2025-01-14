class Movie:

    all = []
    
    def __init__(self, title, reviews=None, reviewers=None):
        self.title = title
        self.reviews = [] if reviews is None else reviews
        self.reviewers = [] if reviewers is None else reviewers
        Movie.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise ValueError("Title must be a string")

    def reviews(self):
        return self._reviews
    
    def reviewers(self):
        return self._reviewers
    
    def average_rating(self):
        if not self.reviews:
            return None
        return sum(self.reviews) / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        highest_rated_movie = None
        highest_rating = 0
        for movie in cls.all:
            rating = movie.average_rating()
            if rating and rating > highest_rating:
                highest_rating = rating
                highest_rated_movie = movie
        return highest_rated_movie