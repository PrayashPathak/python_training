print("Sets in python")

# a = set()  # Set constructor
# b = {}  # Empty Set

# a = [1, True, , "hello", {1, 2, 3}]
# b = [1, 2, 4, True, "python"]

a = set([1, 2, 3, 4, 5])
b = set([1, 2])
print(b.issubset(a))
print(a.intersection(b))
print(a.union(b))
print(a | b)

# Find LCM using school taught method
