#  Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

import random, os

def fillcoeff(k, min=0, max=100) -> list:
    new_list = [random.randint(min, max)]
    while new_list[0] == 0:
        new_list[0] = random.randint(min, max)
    for i in range (1, k+1):
        new_list.append(random.randint(min, max)) 
    return new_list


# запись в файл
def writefile(k: int, user_list, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as pol:
        if user_list[0] == 1:
            pol.write(f'x^{k}')
        else:
            pol.write(f'{user_list[0]}x^{k}')
        for i in range(1,k+1):
            if user_list[i] != 0:
                if user_list[i] > 0:
                    pol.write('+')
                if user_list[i] != 1:
                    pol.write(f'{user_list[i]}')
                if i != k and i != k-1:
                    pol.write(f'x^{k-i}')
                elif i == k-1:
                    pol.write('x')
        pol.write('=0')
        
# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst

app_path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

# генерируем файлы с многочленами
writefile(2, fillcoeff(2), app_path+'Task5_1.txt')
writefile(3, fillcoeff(3), app_path+'Task5_2.txt')

# открываем созданные файлы
with open(app_path+'Task5_1.txt','r') as file:
    Task5_1 = file.readline()

with open(app_path+'Task5_2.txt','r') as file:
    Task5_2 = file.readline()
    
# находим сумму

lst1 = calc_mn(Task5_1)
lst2 = calc_mn(Task5_2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])

# запишем в файл
with open(app_path+'summ.txt', 'w', encoding='utf-8') as file:
    file.write(f'{lst_new}')

# выведем на экран что получилось
print(f"Многочлен 1: {Task5_1}")
print(f"Многочлен 2: {Task5_2}")
print(f"Сумма многочленов: {lst_new}")