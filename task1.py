# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
result = 0
for i in number:
    if i == '.' or i == ',':
        continue
    else:
        result += int(i)
print(result)