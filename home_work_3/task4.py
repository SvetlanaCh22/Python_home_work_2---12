#  Напишите программу, которая будет преобразовывать десятичное число
#  в двоичное.
#  Пример:
#    45 -> 101101
#    3 -> 11
#    2 -> 10

w = input('Введите десятичное число: ')
row = int (w)
bin = ''
while row:
    k = row % 2
    row >>=1
    bin = str(k) + bin 

print(w, 'в двоичной системе счисления: ', bin, '.') 
