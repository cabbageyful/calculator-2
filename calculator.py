from arithmetic import *


# Your code goes here
def calculator(user_input):
    """Makes a REPL for the prefix calculator.

    Takes user's input, parses the mathematical operator & numerical
    values. Function calls referenced refer to arithmetic.py. Tells calculator
    to process numbers & print the result.
    """

    calculator_input = user_input.split(" ")    # creates list from user's input
    math_operator = calculator_input.pop(0)     # stores math operator in own variable

    for i in range(len(calculator_input)):
        calculator_input[i] = int(calculator_input[i])  # remaining values are typecast as integers

    if math_operator == "q":                    # ability to (q)uit the calculator process
        return
    elif math_operator == "+":
        added_numbers = add(calculator_input[0], calculator_input[1])
        print added_numbers
    elif math_operator == "-":
        subtracted_numbers = subtract(calculator_input[0], calculator_input[1])
        print subtracted_numbers
    elif math_operator == "*":
        multiplied_numbers = multiply(calculator_input[0], calculator_input[1])
        print multiplied_numbers
    elif math_operator == "/":
        divided_numbers = divide(calculator_input[0], calculator_input[1])
        print divided_numbers
    elif math_operator == "square":
        squared_numbers = square(calculator_input[0])
        print squared_numbers
    elif math_operator == "cube":
        cubed_numbers = cube(calculator_input[0])
        print cubed_numbers
    elif math_operator == "power":
        exponent_numbers = power(calculator_input[0], calculator_input[1])
        print exponent_numbers
    elif math_operator == "mod":
        remainder_numbers = mod(calculator_input[0], calculator_input[1])
        print remainder_numbers

calculator("cube 104")
