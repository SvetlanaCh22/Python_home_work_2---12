#   Напишите программу, которая принимает на вход вещественное число
#   и показывает сумму его цифр.
#   Пример: 6782 -> 23      0,56 -> 11

r = (input('Введите число: '))

r = r.replace(',',"").replace('.',"")

str_array = str(r)
int_array = map(int,str_array)
array_summa = sum(int_array)
print(array_summa)