# from better_profanity import profanity  # For censoring words

# file = open('swear.txt', 'r')
# user_input = input("Enter a text: ")
# swear_words = []
# swear_words.append(file.read())
# file.close()

# # Writing to a file
# file = open("swear.txt", "w")
# file.write(user_input)
# file.close()

# # Removing the escape sequences from the list

# swear_list = " ".join(swear_words)
# escapes = ''.join([chr(char) for char in range(1, 32)])
# translator = str.maketrans('', '', escapes)
# swear_words = swear_list.translate(translator)

# print(swear_words)

# # Adding custom swear words
# custom_swear_words = profanity.load_censor_words_from_file('./swear.txt')
# print(custom_swear_words)

# censored = ""

# # Censors the swear word completely.

# if profanity.contains_profanity(user_input):
#     censored += profanity.censor(user_input)
# else:
#     print(user_input)


# Simple logic

fin = open('swear.txt', 'r')
data = fin.read()
bad_words = ["this", "line", "make", "demo", "censoring"]

for word in bad_words:
    data = data.replace(word, "*"*len(word))

fout = open("output.txt", "w")
fout.write(data)

fout.close()
fin.close()
