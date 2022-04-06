number = int(input("Please enter a number."))
# i = 2
# while (i <= number):
#     if (number % i == 0):
#         break
#     i += 1
# if (i == number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# Another version

i = 1
count = 0
while i <= number:
    if number % i == 0:
        count += 1
    i += 1
if count <= 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
