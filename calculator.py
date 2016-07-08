"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator(input_string):

    tokens = input_string.split(" ")
    #print tokens
    num1_int = int(tokens[1])
    num2_int = int(tokens[2]) or None
    #print num1_int, num2_int

    if tokens[0] == "q":
        return
    elif tokens[0] == "+":
        added_numbers = add(num1_int, num2_int)
        print added_numbers
    elif tokens[0] == "-":
        subtracted_numbers = subtract(num1_int,num2_int)
        print subtracted_numbers
    elif tokens[0] == "*":
        multiplied_numbers = multiply(num1_int,num2_int)
        print multiplied_numbers
    elif tokens[0] == "/":
        divided_numbers = divide(num1_int,num2_int)
        print divided_numbers
    elif tokens[0] == "square":
        squared_numbers = square(num1_int)
        print squared_numbers

calculator("square 5")
