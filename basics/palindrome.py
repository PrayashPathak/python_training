number = int(input("Enter a number: "))
# print(type(number))
temp = number
reverse = 0

while(number != 0):
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number //= 10
if reverse == temp:
    print(f"{temp} is a palindrome.")
else:
    print(f"{temp} is not a palindrome.")

# inp = input("Enter anything: ")
# print(type(inp))
