#   Задайте натуральное число N. Напишите программу, которая
#   составит список простых множителей числа N.

def mnojiteli(n):
   i = 2
   mnojiteli = []
   while i * i <= n:
       while n % i == 0:
           mnojiteli.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       mnojiteli.append(n)
   return mnojiteli

n = input("Задайте натуральное число: ")
print('Множители числа: ', mnojiteli(int(n)))