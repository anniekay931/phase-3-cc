class Movie:
    
    def __init__(self, title):
        self._title = None
        self.set_title(title)

    def title(self):
        return self._title
    
    def set_title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise ValueError("Title must be a string")

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
