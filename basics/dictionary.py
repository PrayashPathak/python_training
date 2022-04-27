# instructors = {
#     "mosh": "C#",
#     "angela": "flutter",
#     "maximillain": "javascript",
#     "colt": "typescript",
# }

# print(instructors)
# instructors["jonas"] = "web design"

# Looping through a dictionary.

# for key in instructors.keys():
#     print(key.title())

# for key, value in instructors.items():
#     print(key, value)

# Converting a dictionary into a tuple
# lst = []
# for key, value in instructors.items():
#     lst.append(key)
# print(tuple(lst))

# Converting a tuple into a dictionary

# tupl = (1, 23, 14,)
# tupl = dict(tupl)
# print(tupl)


# Demo program for dictionary excercise
# dict = {
#     'a': 1,
#     'b': 20,
#     'hi': 100,
#     'hello': 430,
#     'coffeescript': 1190,
#     'lua': 330
# }

# largest = 0
# for key, value in dict.items():
#     print(key, value)
#     if value > largest:
#         largest = value

# print(f"The largest value = {largest}")

# value_list = []

# for values in dict.values():
#     value_list.append(values)

# print(value_list)

# Comparing the largest values

# max_value = value_list[0]

# for value in value_list:
#     if value > max_value:
#         max_value = value

# Convert two list into a dictionary

keys = ['A', 'B', 'C']
values = [65, 66, 67]
dict = {}

for i in range(0, len(keys)):
    dict[keys[i]] = values[i]
print(dict)

# Combine two dictionary if same key exists then add the key

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {1: 'd', 4: 'c', 5: 'd'}


# Nested Dictionary

student = {
    "name": {"first_name": "prayas", "last_name": "pathak"},
    "roll_number": 28,
    "class": "Section A",
    "subject": ['Opearting System', 'Computer Network', 'Database Systems', 'Theory of Computation', 'Artificial Intelligence']
}

print(student['name']['first_name'])
print(student['name']['last_name'])
print(student['roll_number'])
print(student['class'])
print(student['subject'][:])

# Build a quiz app
