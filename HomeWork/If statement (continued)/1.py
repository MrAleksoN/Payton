i = int(input())
print("Ошибка, введите число в диапазоне [1; 100]" if not 1 <= i <= 100
     else "Fizz Buzz" if not i%3 and not i%5
     else "Fizz" if not i%3
     else "Buzz" if not i%5
     else i)