#  Напишите программу вычисления арифметического выражения заданного строкой.
#  Используйте операции +,-,/,*. Приоритет операций стандартный.
#  Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

from operator import truediv, mul, add, sub  

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Введите выражение: ")
print("Ответ: " + str(calculate(calc)))