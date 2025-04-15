file_1 = open('file_1.txt', 'w')
while True:
    question = input('Enter question or type "exit" to stop: ')
    if question.lower() == 'exit':
        break
    choice_a = input('Enter choice letter "a": ')
    choice_b = input('Enter choice letter "b": ')
    choice_c = input('Enter choice letter "c": ')
    choice_d = input('Enter choice letter "d": ')
    answer = input('Enter the correct answer: ')

    file_1.write(f'Q: {question}\n')
    file_1.write(f'a.) {choice_a}\n')
    file_1.write(f'b.) {choice_b}\n')
    file_1.write(f'c.) {choice_c}\n')
    file_1.write(f'd.) {choice_d}\n')
    file_1.write(f'ans.) {answer}\n')
file_1.close()