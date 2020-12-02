#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Wed Dec  2 14:48:04 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
              More info https://www.guru99.com/python-yield-return-generator.html
'''

import numpy as np
import time
from joblib import Parallel, delayed

def printinfo(func):
    def wrapper():
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func()
    return wrapper

def testyield():
    yield "Welcome to Guru99 Python Tutorials"

def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"

def even_numbers(n):
    for x in range(n):
       if (x%2==0): 
           yield x
    
@printinfo
def testyield01():
    output = testyield()
    print(output)

@printinfo
def testyield02():
    [print(i) for i in testyield()]

@printinfo
def testyield03():
    [print(i) for i in generator()]

@printinfo
def testyield04():
    print(next(testyield()))

@printinfo
def testyield05():
    print(list(even_numbers(10)))

@printinfo
def testyield06():
    num=even_numbers(10)
    try:
        while True:
            print(next(num))
    except StopIteration: pass

def main():
    testyield01()
    testyield02()
    testyield03()
    testyield04()
    testyield05()
    testyield06()
    
if __name__ == "__main__":
    main()
