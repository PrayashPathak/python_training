print("Welcome to calculator: ")

# Modularizing the code for code reusability


def prompt():
    choice = input("Select '*' for multiplication, '+' for addition, '-' for subtraction, '/' for division, '%' for modular division, '**' for exponentitaion and 'quit' to exit the program. ")

    return choice


def get_user_input():
    num = int(input("Enter a number: "))
    return num


def select_operation(selection):
    if selection == '+':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif selection == '-':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif selection == '*':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif selection == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif selection == '%':
        result = modular_division(num1, num2)
        print(f"{num1} % {num2} = {result}")
    elif selection == '**':
        result = exponentiation(num1, num2)
        print(f"{num1} ** {num2} = {result}")
    else:
        print("Invalid Selection made.")


def wants_to_continue():
    response = input(
        "Press 'y' to continue and 'n' to termintate the program: ").lower()
    if response == 'y':
        return True
    return False


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 // num2


def modular_division(num1, num2):
    return num1 % num2


def exponentiation(number, exponent):
    return number ** exponent


can_continue = True


while can_continue:
    choice = prompt()
    num1 = get_user_input()
    num2 = get_user_input()
    select_operation(choice)
    if wants_to_continue():
        can_continue = True
        choice = prompt()
        num1 = get_user_input()
        num2 = get_user_input()
        select_operation(choice)
    else:
        can_continue = False
