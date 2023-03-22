class Review:

    all = []
    
    def __init__(self, reader, book, rating):
        #instances
        self.reader = reader
        self.book = book
        #normal
        self.rating = rating
        Review.all.append(self)


    # rating property goes here!

    def get_rating(self):
        return self.get_rating
    def set_rating(self, rating):
        if rating >= 1 and rating <= 5:
            self._rating = rating
        else:
            print("Rating must be valid")

    rating = property(get_rating, set_rating)


    # reader property goes here!
    def get_reader(self):
        return self._reader
    def set_reader(self, reader):
        from lib.reader import Reader
        if reader in Reader.all:
            self._reader = reader
        else:
            print("Must be valid Reader Object")
    
    reader = property(get_reader, set_reader)


    # book property goes here!
    def get_book(self):
        return self._book
    def set_book(self, book):
        from lib.book import Book
        if book in Book.all:
            self._book = book
        else:
            print("Must be valid Book Object")
    
    book = property(get_book, set_book)