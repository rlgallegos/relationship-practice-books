#!/usr/bin/env python3
from lib.book import Book
from lib.reader import Reader
from lib.review import Review

# import ipdb;


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    false_variable = "This is false"
    
    new_book = Book("Little Women")
    new_book2 = Book("Little Places")
    new_book3 = Book("Little Things")

    new_reader = Reader('Samantha')
    new_reader2 = Reader('Karenilla')

    new_review = Review(new_reader, new_book, 3)
    new_review2 = Review(new_reader, new_book, 2)
    new_review3 = Review(new_reader, new_book3, 4)
    new_review4 = Review(new_reader2, new_book3, 4)
    new_review5 = Review(new_reader2, new_book2, 5)


    # print(vars(new_review))
    # new_instance = new_reader2.rate_book(new_book, 1)
    # new_review_obj = vars(new_review)
    # print(new_review_obj)
    # print(new_instance)


    print( vars( Book.highest_rated() ) )


    # print( new_reader2.reviewed_book(new_book) )


    # review_list = new_book3.reviews()
    # for review in review_list:
    #     print(review)


    # review_list = new_reader.reviews()
    # for review in review_list:
    #     print(review)

    # book_list = new_reader.reviewed_books()
    # for book in book_list:
    #     print(book)

# DO NOT REMOVE THIS
    # ipdb.set_trace()
