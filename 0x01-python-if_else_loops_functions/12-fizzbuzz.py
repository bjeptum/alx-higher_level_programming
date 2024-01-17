#!/usr/bin/python3
"""
Prints the no 1 to 100
Separated by a space
multiples of three print Fizz
multiples of 5 print Buzz
multiples of both 3 and 5 print FizzBuzz
"""


def fizzbuzz():
    for num in range(1, 100):
        if (num % 15 == 0):
            print("FizzBuzz", end=" ")
        elif (num % 3 == 0):
            print("Fizz", end=" ")
        elif (num % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{}".format(num), end=" ")
