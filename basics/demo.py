a = 10
try:
    print(a/5)
except Exception:
    print("Exception occured.")
else:  # Gets executed if exception does not occurs.
    print("In Else block.")
finally:
    print("This gets executed irrespective of the exception occurence..")
print("Program executed.")
