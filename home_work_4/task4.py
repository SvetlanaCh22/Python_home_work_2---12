#   Задана натуральная степень k. Сформировать случайным образом список
#   коэффициентов (значения от 0 до 100) многочлена и записать
#   в файл многочлен степени k.
#   Пример: k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random, os

def fillcoeff(k, min=0, max=100) -> list:
    new_list = [random.randint(min, max)]
    while new_list[0] == 0:
        new_list[0] = random.randint(min, max)
    for i in range (1, k+1):
        new_list.append(random.randint(min, max)) 
    return new_list

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

# определим степень
k = int(input('Укажите натуральную степень многочлена k: '))
# сгенерируем коэффициенты
coeff = fillcoeff(k)
print(f"Сгенерированные коэффициенты: {coeff}")
# зададим папку со скриптом для файлов
app_path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
# создадим и запишем новый многочлен
newfile = app_path+'Task4.txt'
writefile(k, coeff, newfile)
# считаем из файла что получилось и выведем на экран
with open(app_path+'Task4.txt','r') as file:
    print(f"Сгенерированный многочлен: {file.readline()}")