#   Задайте список из N элементов, заполненных
#   числами из промежутка [-N, N]. Найдите произведение
#   элементов на указанных позициях. Позиции хранятся
#   в файле file.txt в одной строке одно число.


import random, os

n = int(input("Введите число: "))

array = list(range(1, n+1))
i = 0
while (i < n):
    array[i] = random.randint(-n,n)
    i = i + 1

print("Получившийся массив: ", list(array))

file1 = open("file.txt", "r")

mul = 1

while True:
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    #print("Умножаем ", mul, " на ", array[int(line.strip())], " из ячейки массива ", line.strip(), " и получаем ", str(mul * array[int(line.strip())]))
    pointer = int(line.strip())
    # проверим выход за границы массива
    if (pointer < n):
        mul = mul * array[pointer]

file1.close

print("Произведение чисел по позициям из файла: ", mul)