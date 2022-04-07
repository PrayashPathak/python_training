# print("Lists in python.")
# languages = ['c', 'lua', 'python', 'haskell', 'erlang', 'elixir',
#              'scala', 'java', 'javascript', 'typescript', 'dart', 'ruby', 'pearl', 'rust', 'golang', 'coffeescript', 'sql', 'ocaml', 'lisp', 'prolog']

# for language in languages:
#     print(language.title())

# List Constructor
# b= list()

# a = []
# b = [10, 20, 38, 10]
# a.extend(b)
# print(a)
# b *= 3
# print(b)

# Sublist or not of a list
a = [1, 2, 3, 4, 5]
b = [1, 21]
# c = []
# for item1 in a:
#     for item2 in b:
#         if item2 in a:
#             c.append(item2)

# print(c)
# print(c.__eq__(a))


great = a
small = b
if len(b) > len(a):
    great = b
    small = a

check = True
for i in range(len(small)):
    if small[i] not in great:
        check = False

if check == True:
    print("Sub-List")
else:
    print("Not a sublist.")
