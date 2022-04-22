# Write a python program to add 'ing' at the end of a given string(;ength should be at least three). If the string already ends with 'ing' add 'ly' instead. Leave the string unchanged if the length of the string is less than 3.

inp = input("Enter a string: ")
if len(inp) >= 3:
    if "ing" in inp:
        new_str = inp.replace(inp, inp + 'ly')
    else:
        new_str = inp + 'ing'
else:
    new_str = inp

print(f"String = {new_str}")
