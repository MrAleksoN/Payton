a = int(input())

for i in range(2, a + 1):

   flag = True

   for f in range(2, i):

       if i % f == 0:

           flag = False

           break

   if flag:

       print(i, end=' ')