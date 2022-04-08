instructors = {
    "mosh": "C#",
    "angela": "flutter",
    "maximillain": "javascript",
    "colt": "typescript",
}

print(instructors)
instructors["jonas"] = "web design"

# Looping through a dictionary.

# for key in instructors.keys():
#     print(key.title())

# for key, value in instructors.items():
#     print(key, value)

# Converting a dictionary into a tuple
lst = []
for key, value in instructors.items():
    lst.append(key)
print(tuple(lst))

# Converting a tuple into a dictionary

tupl = (1, 23, 14,)
tupl = dict(tupl)
print(tupl)
