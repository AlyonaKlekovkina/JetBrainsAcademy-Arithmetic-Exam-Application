import random


def generate_task():
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    oper = random.choice('+-*')
    result = eval(f'{a}{oper}{b}')
    return a, b, oper, result


def simple_calculation():
    info = input().split()
    a = int(info[0])
    oper = info[1]
    b = int(info[2])
    result = 0
    if oper == '+':
        result = a + b
    if oper == '-':
        result = a - b
    if oper == '*':
        result = a * b
    return result


def check_reply():
    while True:
        reply = input()
        try:
            return int(reply)
        except ValueError:
            print('Incorrect format.')


def get_difficulty_level():
    while True:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        inp = input()
        try:
            answer = int(inp)
            if answer == 1:
                return 1
            elif answer == 2:
                return 2
            else:
                print('Incorrect format.')
        except ValueError:
            print('Incorrect format.')


def level_one_task():
    global count_right
    task = generate_task()
    print(task[0], task[2], task[1])
    reply = check_reply()
    if int(task[3]) == reply:
        print('Right!')
        count_right += 1
    if int(task[3]) != reply:
        print('Wrong!')


def level_two_task():
    global count_right
    number = random.randrange(11, 30)
    print(number)
    reply = level_two_check(number)
    if number * number == reply:
        count_right += 1
        print('Right!')
    if number * number != reply:
        print('Wrong!')


def level_two_check(number):
    while True:
        inp = input()
        try:
            calculated = int(inp)
            return calculated
        except ValueError:
            print('Wrong format! Try again.')
            print(number)


count_right = 0
level = get_difficulty_level()
text = ''
for i in range(5):
    if level == 1:
        level_one_task()
        text = '(simple operations with numbers 2-9)'
    if level == 2:
        level_two_task()
        text = '(integral squares of 11-29)'
    i += 1
print('Your mark is {}/5. Would you like to save the result? Enter yes or no.'.format(count_right))
answer = input()
possible_answers = ['yes', 'YES', 'y', 'Yes']
if answer in possible_answers:
    name = input('What is your name?\n')
    line = '{}: {}/5 in level {} {}'.format(name, count_right, level, text)
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(line)
    file.write('\n')
    file.close()
    print('The results are saved in "results.txt".')
