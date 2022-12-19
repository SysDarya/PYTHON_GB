# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего 
# (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random

n = int(input('Введите длину списка >>> '))
l = []
for num in range(0,n):
    
    random_number = round(random.randint(-10,10))
    l.append(random_number)
print(l)

count = 0

for i in range(1, len(l)):
    if l[i-1]<l[i]:
        count+=1

print(count)
