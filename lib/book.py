from lib.review import Review

class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
        

    # title property goes here!

    def get_title(self):
        return self._title
    def set_title(self, title):
        if len(title) > 0 and type(title) == str:
            self._title = title
        else:
            print('Title must be valid')
    title = property(get_title, set_title)

    def reviews(self):
        return [review for review in Review.all if review._book == self]

    def reviewers(self):
        return [review._reader for review in self.reviews()]

    def average_rating(self):
        ratings = [review._rating for review in self.reviews()]
        return sum(ratings) / len(ratings)

    @classmethod
    def highest_rated(cls):
        highest_rated_book = cls.all[0]
        for book in cls.all:
            if book.average_rating() > highest_rated_book.average_rating():
                highest_rated_book = book
        return highest_rated_book
        
    
