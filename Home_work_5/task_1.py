#  Напишите программу, удаляющую из текста все слова,
#  в которых присутствуют все буквы "абв".

import os
app_path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

# открываем файл в режиме чтения utf-8
file = open(app_path+'Test abv.txt', 'r', encoding='utf-8')

# читаем все строки и удаляем переводы строк
lines = file.readlines()
lines = str([line.rstrip('\n') for line in lines])

file.close()

print('Исходник: ', lines)

find_txt1 = "а"
find_txt2 = "б"
find_txt3 = "в"


lst = [i for i in lines.replace("."," .").split() if (find_txt1 not in i) or (find_txt2 not in i) or (find_txt3 not in i)]
new_text = " ".join(lst)
print(f'Результат: {new_text}')

# открываем файл в режиме записи utf-8
file = open(app_path+'Test second.txt', 'w', encoding='utf-8')
file.write(new_text)
file.close()