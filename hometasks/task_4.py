# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input('Сколько журавликов сделали дети >>> '))
kat = (s // 3) * 2
pet = (s // 3) // 2
print('Катя сделала', kat, 'журавликов. Петя и Сережа сделали по', pet, 'журавликов.')