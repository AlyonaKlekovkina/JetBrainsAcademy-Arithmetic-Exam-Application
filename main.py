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


task = generate_task()
print(task[0], task[2], task[1])
reply = input()
if int(task[3]) == int(reply):
    print('Right!')
else:
    print('Wrong!')
