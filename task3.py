# Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите
# на экран их сумму.

number = int(input('Введите число N: '))

sum = 0
lst = {i: (1 + 1 / i) ** i for i in range(1, number + 1)}

for key in lst:
    sum += round(lst[key], 3)

print(sum)