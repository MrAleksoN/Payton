def search_common_elem(a, b):
common = []
for i in a:
if i in b and i not in common:
common.append(i)
return common
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(search_common_elem(first, second))