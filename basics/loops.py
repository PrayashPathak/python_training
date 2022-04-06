# i = 1
# while(i <= 20):
#     print(i)
#     i += 2  # i = i + 2


#  Pattern programming.
# *
# **
# ***
# ****
# *****
# *
# **
# ***
# ****
# *****

# i = 1

# while(i <= 5):
#     print("*"*i)
#     i += 1


#  For with range

# for i in range(1, 20, 2):
#     print(i)

# Reversing a string

name = "python programming"
print(name[::-1])

# for i in range(5):
#     print(i)

string = "HELLO World"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in string.lower():
    i = 0
    if char in vowels:
        count += 1
print(f"Vowels = {count}")

# new_string = ''
# for i in range(len(string)-1, -1, -1):
#     new_string += string[-i]
# print(new_string)

# new_string = ""
new_string = "".join(reversed(string))
print(new_string)
