# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

import random
def watermelonList(N):
    watermelons = []
    for i in range(N):
        weight = round(random.uniform(5000,30000),0)
        watermelons.append(weight)
    print(watermelons)

    min = max = watermelons[0]
    for item in watermelons:
        if min > item:
            min = item
        if max < item:
            max = item
    return min, max

N = int(input('Введите количество арбузов >>> '))
print(watermelonList(N))