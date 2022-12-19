# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

n = int(input('Введите количество монеток >>> '))
m = []
for num in range(0,n):
    
    random_number = round(random.randint(0, 1),0)
    m.append(random_number)

print(m)

zero = 0
one = 0
for item in m:
    if (item == 0):
        zero += 1
    else:
        one += 1

if one < zero:
    print(one)
else:
    print(zero)