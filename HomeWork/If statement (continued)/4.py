l = [0, 0, 0]
for i in range(3):
nm = i + 1
print('Введите уровень продаж менеджера', i + 1, '>> ', end='')
s = int(input())
if s < 500:
f = 200 + s * 0.03
l[i] = int(f)
elif s < 1000:
f = 200 + s * 0.05
l[i] = int(f)
elif s > 1000:
f = 200 + s * 0.08
l[i] = int(f)
lm = (l.index(max(l)))
l[lm] += 200
print('Лучший менеджер >>', lm + 1)
for j in range(3):
print('ЗП менеджера', j + 1, '>>', l[j])