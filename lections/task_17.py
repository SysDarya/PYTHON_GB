# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

n = int(input('Введите длину списка >>> '))
l = []
for num in range(0,n):
    
    random_number = round(random.randint(0,5))
    l.append(random_number)

a = set(l)

print(l)
print(len(a))