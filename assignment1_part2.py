#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rebecca Hayden, Assignment 1, Part 2"""

class Book:
    """Class for books"""
    def __init__(self, author, title):
        """this function returns a book by author and title based on variables"""
	self.author = author
	self.title = title

    def display(self):
	"""This function provides instructions on printing format"""
	print"{0}, written by {1}".format(self.title, self.author)}

	print(self.title, 'written by' self.author)

Book1 = Book('Of Mice and Men', 'John Steinbeck')
Book2 = Book('To Kill a Mockingbird','Harper Lee')

Book1.display()
Book2.display()

x.author('John Steinbeck')
x.title('Of Mice and Men')

y.author('Harper Lee')
y.title('To Kill a Mockingbird')


to call

x.display()
y.display()




		a.title

 title 'written by' author
		Book1 

class Book:
    def __init__(self):
	self.author1 = ('John Steinbeck')
	self.title1 = ('Of Mice and Men')
	self.author2 = ('Harper Lee')
	self.title2 = ('To Kill a Mockingbird')

    def display(self):
	print(self.author)
