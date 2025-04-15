file_1 = open('file_1.txt', 'w')
while True:
    question = input('Enter question or type "exit" to stop: ')
    if question.lower() == 'exit':
        break
    choice_a = input('Enter choice "a": ')
    choice_b = input('Enter choice "b": ')
    choice_c = input('Enter choice "c": ')
    choice_d = input('Enter choice "d": ')
    answer = input('Enter the correct answer: ')

    file_1.write(f'question\n')
    file_1.write(f'choice_a\n')
    file_1.write(f'choice_b\n')
    file_1.write(f'choice_c\n')
    file_1.write(f'choice_d\n')
    file_1.write(f'answer\n')