"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

"""repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

            (...etc.)"""

def validate_input(input_list)
    num_list = input_list.pop(0)
    valid_operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

    index = 0

    while index < len(num_list):
        try:
            int(num_list[index])
            index += 1
        except:
            print("Enter valid numbers!")
            index = 0

    if input_list[0] not in valid_operators
        print('enter a valid operator')


while True:
    answer = input(">")
    input_list = answer.split(' ')
    validate_input(input_list)

    if input_list[0] == 'q':
        break
    elif input_list[0] == '+':
        result = add(num1, num2)
        print(result)
    elif input_list[0] == '-':
        result = subtract(num1, num2)
        print(result)
    elif input_list[0] == '*':
        result = multiply(num1, num2)
        print(result) 
    elif input_list[0] == '/':
        result = divide(num1, num2)
        print(result)
    elif input_list[0] == 'square':
        result = square(num1)
        print(result)
    elif input_list[0] == 'cube':
        result = cube(num1)
        print(result)
    elif input_list[0] == 'pow':
        result = pow(num1, num2)
        print(result)
    elif input_list[0] == 'mod':
        result = mod(num1, num2)
        print(result)
    else:
        print('please enter a valid request')


def 