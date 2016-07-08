"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator(input_string):

    split_input_string = input_string.split(" ")
    math_operation = split_input_string.pop(0)  
    #print split_input_string
    #print math_operation     
    

    for i in range(len(split_input_string)):
        split_input_string[i] = int(split_input_string[i])
        
     
        
    if math_operation == "q":
        return
    elif math_operation == "+":
        added_numbers = add(split_input_string[0], split_input_string[1])
        print added_numbers
    elif math_operation == "-":
        subtracted_numbers = subtract(split_input_string[0],split_input_string[1])
        print subtracted_numbers
    elif math_operation == "*":
        multiplied_numbers = multiply(split_input_string[0],split_input_string[1])
        print multiplied_numbers
    elif math_operation == "/":
        divided_numbers = divide(split_input_string[0],split_input_string[1])
        print divided_numbers
    elif math_operation == "square":
        squared_numbers = square(split_input_string[0])
        print squared_numbers

calculator("/ 6 3")
#To Do: Add remaining math functions (cube, power, mod), comment entire file, add Docstring
#Enable user to type input string directly in terminal through arithmetic.py
#Enable user to input multiple arguments
