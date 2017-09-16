#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1, Part 2"""

class Book:
    """Class for books"""

    def __init__(self, author, title):
        """this function returns a book by author and title based on variables"""

	self.author = author
	self.title = title

    def display(self):
	"""This function provides instructions on printing format and displays 2 books"""
	print(self.title, 'written by', self.author)

    Book1 = Book('John Steinbeck', 'Of Mice and Men')
    Book2 = Book('Harper Lee', 'To Kill a Mockingbird')

    Book1.display()
    Book2.display()
