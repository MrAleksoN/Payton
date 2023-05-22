# Напишите функцию,вычисляющию сумму элементов списка целых.Список передаётся в качестве параметра.

import random
print("Введите размер списка" )
n=int(input("n="))
m=[]
def print_summ(n):
    for i in range(n):
        m.append(i)
for i in range(n):
     print(random.randint(-15, 17), end='')

print_summ(m)