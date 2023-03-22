from lib.review import Review
class Reader:

    all = []
    
    def __init__(self, username):
        self.username = username
        Reader.all.append(self)

    # username property goes here!

    def get_username(self):
        return self._username
    def set_username(self, username):
        list_of_taken_names = [reader.username for reader in Reader.all]
        if username not in list_of_taken_names and len(username) >= 8 and len(username) <= 16:
            self._username = username
        else:
            print('Username must be valid')

    username = property(get_username, set_username)

    # List of review instances by reader
    def reviews(self):
        return [review for review in Review.all if review._reader == self]

    # List of book instances reviewed by reader
    def reviewed_books(self):
        return [review._book for review in self.reviews()]

    def reviewed_book(self, book):
        return ( book in self.reviewed_books() )

    def rate_book(self, book, rating):
        if not self.reviewed_book(book):
            return Review(self, book, rating)
        else:
            for review in self.reviews():
                if review._book == book:
                    review._rating = rating
            
