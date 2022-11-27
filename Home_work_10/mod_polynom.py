# 5) Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random, os
from mod_log import LOG

@LOG
def write_file(name,st):
    """запись в файл"""
    with open(name, 'w') as data:
        data.write(st)
        
@LOG
def rnd():
    """создание случайного числа от 0 до 100"""
    return random.randint(0,101)

@LOG
def create_mn(k):
    """создание коэффициентов многочлена"""
    lst = [rnd() for i in range(k+1)]
    return lst

@LOG
def create_str(sp):
    """создание многочлена в виде строки"""
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

@LOG
def sq_mn(k):
    """получение степени многочлена"""
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

@LOG
def k_mn(k):
    """получение коэффицента члена многочлена"""
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

@LOG
def calc_mn(st):
    """разбор многочлена и получение его коэффициентов"""
    st = st.replace(' ', '').split('=')
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

@LOG
def mn_summ(mn1, mn2):
    """находим сумму"""
    lst1 = calc_mn(mn1)
    lst2 = calc_mn(mn2)
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

    mn_new = create_str(lst_new)
    return mn_new

@LOG
def make_files_and_calc():
    """генерируем файлы с многочленами"""
    app_path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

    # генерируем файлы с многочленами
    write_file(app_path+'Task5_1.txt', create_str(create_mn(2)))
    write_file(app_path+'Task5_2.txt', create_str(create_mn(3)))

    # открываем созданные файлы
    with open(app_path+'Task5_1.txt','r') as file:
        Task5_1 = file.readline()

    with open(app_path+'Task5_2.txt','r') as file:
        Task5_2 = file.readline()
    
    mn_new = mn_summ(Task5_1, Task5_2)
    
    # запишем в файл
    write_file(app_path+'summ.txt', mn_new)

    # выведем на экран что получилось
    print(f"Многочлен 1: {Task5_1}")
    print(f"Многочлен 2: {Task5_2}")
    print(f"Сумма многочленов: {mn_new}")

#make_files_and_calc()