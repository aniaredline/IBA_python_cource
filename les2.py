import random

mas = [random.randint(-1000, 1000) for _ in range(20)]
print(mas)

max_elem = mas[0]
min_mod = abs(mas[0])
for i in mas:
    if i % 2 == 1 and max_elem < i:
        max_elem = i
    if min_mod > abs(i):
        min_mod = abs(i)
print(max_elem)
print(min_mod)
