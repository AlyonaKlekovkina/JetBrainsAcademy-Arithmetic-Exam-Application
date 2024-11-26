import random


def generate_task():
    a = random.randrange(2, 9+1)
    b = random.randrange(2, 9+1)
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


count_right = 0
for i in range(5):
    task = generate_task()
    print(task[0], task[2], task[1])
    reply = check_reply()
    if int(task[3]) == reply:
        print('Right!')
        count_right += 1
    if int(task[3]) != reply:
        print('Wrong!')
    i += 1
print('Your mark is {}/5.'.format(count_right))

