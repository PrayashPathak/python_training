# A program to display the following pattern.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# number = int(input("Enter the number upto the pattern needs to be printed: "))

# for i in range(1, number+1):
#     for j in range(1, number+1):
#         if i >= j:
#             print(j, end=" ")
#     print()


# A
# BB
# CCC
# DDDD
# EEEEE

# characters = ['A', 'B', 'C', 'D', 'E']

# for i in range(0, 5):
#     for j in range(0, 5):
#         if j >= i:
#             print(characters[i], end=" ")
#     print()

# *
# ***
# *****
# *******
# *********


# for i in range(1, 6, 1):
#     for j in range(1, 10, 1):
#         if (j <= 2*i - 1):
#             print("*", end=" ")
#         else:
#             print("", end=" ")
#     print()


for i in range(1, 6, 1):
    for j in range(1, 10, 1):
        if (j >= 6 - i and j <= 4 + i):
            print("*", end=" ")
        else:
            print("", end=" ")
    print()
