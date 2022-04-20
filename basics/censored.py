# import operator  # For contains function
from better_profanity import profanity  # For censoring words

file = open('swear.txt', 'r')
user_input = input("Enter a text: ")
swear_words = []
swear_words.append(file.read())

# Removing the escape sequences from the list

swear_list = " ".join(swear_words)
escapes = ''.join([chr(char) for char in range(1, 32)])
translator = str.maketrans('', '', escapes)
swear_words = swear_list.translate(translator)

print(swear_words)

censored = ""
if str.__contains__(user_input, swear_words):
    censored += user_input
print(censored)
