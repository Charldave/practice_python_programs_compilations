import random

with open('file_1.txt', 'r') as file_1:
    lines = file_1.readlines()

question_list = []
for i in range(0, len(lines), 6):
    question = lines[i:i+6]
    if len(question) == 6:
        question_list.append(question)

random.shuffle(question_list)