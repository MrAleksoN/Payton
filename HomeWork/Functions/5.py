def proizv(A, B):
    if A == B:
        return "Диапазон введен неверно."
    if A > B:
        A, B = B, A
    res = 1
    for i in range(A, B + 1):
        res *= i
    return res
 
 
print('Произведение чисел от 2 до 10 = ', proizv(2, 10))
 