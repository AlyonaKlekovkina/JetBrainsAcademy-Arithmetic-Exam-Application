# write your code here
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
print(result)

