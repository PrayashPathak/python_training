# Quiz

# import data
# from question_model import Question
# from quiz_brain import QuizBrain


# # switch to True to use the original questions
# use_original = False
# name = input("Enter your name: ")
# question_bank = []
# # fill up the question bank list with Question objects
# if use_original:
#     for dic in data.original_question_data:
#         question_bank.append(Question(dic["text"], dic["answer"]))
# else:
#     for dic in data.question_data:
#         question_bank.append(Question(dic["question"], dic["correct_answer"]))

# qb = QuizBrain(question_bank)
# # repeat while there are still questions remaining
# while qb.still_has_questions():
#     qb.next_question()
# # no need for a + 1 to the question_number here, as it gets increased after the last question is completed

# file = open('./scores.txt', 'a')
# score = qb.score
# file.write(f"{name} {score}")
# print(f"Your final score is: {qb.score}/{qb.question_number}.")
# file.close()

# Reading the list of players

file = open('./scores.txt', 'r')
players = (file.readlines())
scores = []
users = []

for player in players:
    users.append(player)

file.close()

# Add start time and end time for each questions using counters
