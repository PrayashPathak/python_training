
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter '+' for addition, '-' for subtraction, '/' for division ,'*' for multiplication, '%' for modular division, '**' for exponentiation")

if choice == '+':
    print("You performed Addition. ")
    print(f"{num1} + {num2} = {num1+num2}")
elif choice == '-':
    print("You perfomed subtraction.")
    print(f'{num1}- {num2} = {num1-num2}')
elif choice == '/':
    print("You perfromed division.")
    print(f"{num1} / {num2} = {num1/num2}")
elif choice == '*':
    print("You performed multiplication.")
    print(f"{num1} * {num2} = {num1*num2}")
elif choice == '%':
    print("You performed modular division.")
    print(f"{num1} % {num2} = {num1 % num2}")
elif choice == '**':
    print("You perormed exponentiation.")
    print(f"{num1} ** {num2} = {num1**num2}")
else:
    print("Please provide a valid input.")
