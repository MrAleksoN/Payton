def chetnie(a, b):
    if a == b:
        return "Диапазон введен неверно."
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(int(i), end=' ')