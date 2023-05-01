arr = []

while True:

   number = int(input())

   arr.append(number)

   if number == 7:

       print('Сумма введённых чисел:', sum(arr))

       print('Максимальное число:', max(arr))

       print('Минимальное число:', min(arr))

       exit()