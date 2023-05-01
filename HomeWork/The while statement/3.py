a=int(input("Первое число: "))

b=int(input("Второе число: "))

for i in range(a,b+1):

   if i%3!=0 and i%5!=0:

       print(i)

   if i%3==0 and i%5==0:

       print("Fizz Buzz")

   else:

       if i%3==0:

           print("Fizz")

       if i%5==0:

           print("Buzz")