#  Реализуйте алгоритм перемешивания списка.

import random

dok = list(range(15))
print("Исходный список: ", dok)
random.shuffle(dok)
print("Список после перемешивания: ", dok)