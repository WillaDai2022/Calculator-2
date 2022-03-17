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
            
def get_input():
    answer = input(">")
    input_list = answer.split(' ')
    validate_input(input_list)


def validate_input(input_list):
    operator = input_list.pop(0)
    print(input_list)
    valid_operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

    index = 0

    while index < len(input_list):
        try:
            vali_num = int(input_list[index])
            index += 1
        except:
            print("Enter valid numbers!")
            get_input()

    while True:
        if operator not in valid_operators:
            print('enter a valid operator')
            get_input()
            break
        else:
            break
    
    calculate(input_list)

def calculate(input_list):
    while True:
        if input_list[0] == 'q':
            break
        elif input_list[0] == '+':
            if len(input_list) < 3:
                continue
            result = add(num1, num2)
            print(result)
        elif input_list[0] == '-':
            if len(input_list) < 3:
                continue
            result = subtract(num1, num2)
            print(result)
        elif input_list[0] == '*':
            if len(input_list) < 3:
                continue
            result = multiply(num1, num2)
            print(result) 
        elif input_list[0] == '/':
            if len(input_list) < 3:
                continue
            result = divide(num1, num2)
            print(result)
        elif input_list[0] == 'square':
            if len(input_list) < 2:
                continue
            result = square(num1)
            print(result)
        elif input_list[0] == 'cube':
            if len(input_list) < 2:
                continue
            result = cube(num1)
            print(result)
        elif input_list[0] == 'pow':
            if len(input_list) < 3:
                continue
            result = pow(num1, num2)
            print(result)
        elif input_list[0] == 'mod':
            if len(input_list) < 3:
                continue
            result = mod(num1, num2)
            print(result)
        else:
            print('please enter a valid request')

get_input()