counter1 = 0
counter2 = 0
for i in range(100, 10000): # 100-999  1000-9999
    if len(str(i)) == 3:
        if i // 100 != i // 10 % 10 and i // 100 != i % 10 and i // 10 % 10 != i % 10:
         counter1 += 1
    else: # 1234
        if i // 1000 != i // 100 % 10 and i // 1000 != i // 10 % 10 and i // 1000 != i % 10 and i // 100 % 10 != i // 10 % 10 and i // 100 % 10 != i % 10 and i // 10 % 10 != i % 10:
            counter2 += 1
print(counter1 + counter2)