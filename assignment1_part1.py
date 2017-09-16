#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1, Part 1"""

def listDivide(numbers, divide=2):
    """This function takes a list of numbers and divides by the divide parameter
    and returns the amount of numbers from that list that are divisible by divide"""

    global newlist
    int(divide)
    newlist = []
    for x in numbers:
        a = x/divide
        if a == int(a):
            newlist.append(a)
    return len(newlist)

class ListDivideException(object):
    """class: ListDivideException, raises error 
    upon testing if the function listDivide doesn't run properly"""
    pass

    def testListDivide(listDivide):
        """This function calls the listDivide function and passes in several test parameters"""
        if listDivide([1,2,3,4,5]) != 2:
            raise ListDivideException()
        if listDivide([2,4,6,8,10]) != 5:
            raise ListDivideException()
        if listDivide([30,54,63,98,100], divide=10) != 2:
            raise ListDivideException()
        if listDivide([]) != 0:
            raise ListDivideException()
        if listDivide([1,2,3,4,5], 1) != 5:
            raise ListDivideException()
