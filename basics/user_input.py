fout = open('users.txt', 'w')
print("Please enter the following details to save to a file.")
name = input("Enter your name: ").title()
email = input("Enter your email address: ").lower()
age = (input("Enter your age: ")).lower()
address = input("Enter your address: ").title()
cell_number = input("Enter your contact number: ").lower()
profession = input("Enter your job: ").title()
gender = input("Enter your gender: ").lower()

user_details = {
    "name": name,
    "email": email,
    "age": age,
    "address": address,
    "cellno": cell_number,
    "job": profession,
    "gender": gender
}
print(user_details)
print("Writing details to a file ...............")

for key, values in user_details.items():
    values = key.title() + ": " + values
    fout.write(values)
    fout.write("\n")
print("Successfully wrote to a file. Clsoing the file ........")
fout.close()

print("Reading the contents of a file ...........")
fin = open('users.txt', 'r')
print("The contents of a file are: ")
content = fin.readlines()

# Removing the escape sequences
content = " ".join(content)
escapes = ''.join([chr(char) for char in range(1, 32)])
translator = str.maketrans('', '', escapes)
content = content.translate(translator)
print(content)
fin.close()
