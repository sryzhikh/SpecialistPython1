# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here

import random
n = int(input("n:"))
список = str()
i=1
while i<=n:
    список = str(список) + str(random.randint(-100, 100)) + str(" ")
    i+=1
print(список)
