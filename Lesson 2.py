def printLine(count, symbol):
    for i in range(count):
        print(symbol, end='')
    print()

#printLine(symbol='$', count=30)

'''printLine(30, '$')
printLine(15, '#')
printLine(20, '@')
printLine(40, '`')
printLine(10, "mama ")'''

def add(a, b):
    c = a + b
    return c

#print(add(4, 5))

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

'''count = 0
l = [23,32,45,56,67,5,32,23,43,6]
for i in l:
    if isEven(i):
        count += 1

print(count)'''

import random

def orel_reshka():
    c = random.randint(0, 1)
    if c == 0:
        print("Решка")
    else:
        print("Орел")
    return c

orel = 0
reshka = 0
for i in range(9):
    if orel_reshka() == 0:
        reshka += 1
    else:
        orel += 1

printLine(20, '-')
print("Орел  -", orel)
print("Решка -", reshka)
if orel > reshka:
    print("Перемога орлів")
elif reshka > orel:
    print("Перемога решків")
else:
    print("Нічия")