# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
number = int(input('Введите число N: '))

result = []

for i in range(1, number + 1):
    result.append(math.factorial(i))

print(result)

