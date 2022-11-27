#  Вычислить число c заданной точностью d
#  Пример: при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

def calcnumber(n, d):
    # делаем чтобы работало и с точкой и с запятой в числе
    n = float(n.replace(',', '.'))
    # конвертируем точность из дроби в количество знаков
    d = Decimal(str(d)).as_tuple().exponent*(-1)
    # форматируем число n под шаблон с нужным количеством знаков d
    template = '{:.' + str(d) + 'f}'
    return template.format(n)

d = input("Задайте точность: ")
n = input("Задайте число, которое нужно вывести с заданной точностью: ")
print(calcnumber(n, d))