number = int(input("Enter a number to check whether it is armstrong or not."))
exponent = len(str(number))
reverse = 0
temp = number
while(number != 0):
    remainder = number % 10
    reverse = reverse + remainder ** exponent
    number //= 10
if reverse == temp:
    print(f"{temp} is an armstrong number.")
else:
    print(f"{temp} is not an armstrong number.")
