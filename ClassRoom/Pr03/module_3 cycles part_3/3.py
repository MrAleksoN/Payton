# Пользователь вводит с клавиатуры две границы диапазонна и число Если число не попадпет в диапазон.....
while True:
    a = int(input('A '))
    b = int(input('B '))
    num = int(input('Number user '))
    if num > a and num < b:
        break
for i in range(a, b+1):
    if i == num:
        print('!'+ str(num) + '!')
        continue
    print(i, end=' ')