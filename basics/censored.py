
from better_profanity import profanity  # For censoring words

file = open('swear.txt', 'r')
user_input = input("Enter a text: ")
swear_words = []
swear_words.append(file.read())
file.close()

# Removing the escape sequences from the list

swear_list = " ".join(swear_words)
escapes = ''.join([chr(char) for char in range(1, 32)])
translator = str.maketrans('', '', escapes)
swear_words = swear_list.translate(translator)

print(swear_words)

# Adding custom swear words
custom_swear_words = profanity.load_censor_words_from_file('./swear.txt')
print(custom_swear_words)

censored = ""

# Censors the swear word completely.

if profanity.contains_profanity(user_input):
    censored += profanity.censor(user_input)
    print(censored)
else:
    print(user_input)

# if user_input in custom_swear_words:
#     censored += user_input
#     print(censored)
