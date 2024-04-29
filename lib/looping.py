#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 0
    while i<11:
        print (i)
        i += 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_integers = list()
    for integer in int_list:
        squared_integer = integer * integer
        squared_integers.append(squared_integer)
    return squared_integers

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i% 5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
