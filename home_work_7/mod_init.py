import mod_view
import sys
import json
import os

def open_exist():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+'\spravochnik.json', 'r', encoding='utf-8') as file:
        phone_book = json.loads(file.read())
    mod_view.display_all(phone_book)
    return phone_book

def initial_phonebook():
    temp = []
    print('Чтобы начать предлагаем сохранить первый контакт\n')
    print('В случае если Вы не собираетесь сейчас ничего вводить, нажмите 0')
    phone_book = []
    rows = 1
    cols = 6
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Введите ID: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("ID является обязательным полем.")
            if j == 1:
                temp.append(str(input("Введите имя: "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    sys.exit("Имя является обязательным полем.")
            if j == 2:
                temp.append(str(input("Введите фамилию: ")))
            if j == 3:
                temp.append(str(input("Введите день рождения (дд/мм/гг): ")))
            if j == 4:
                temp.append(str(input("Введите место работы: ")))
            if j == 5:
                temp.append(str(input("Введите номер телефона: ")))
    phone_book.append(temp)
    mod_view.display_all(phone_book)
    save_phonebook(temp)
    return phone_book

def save_phonebook(pb):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+'\spravochnik.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(pb))