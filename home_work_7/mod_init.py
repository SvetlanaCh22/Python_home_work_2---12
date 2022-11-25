import mod_menu
import mod_add
import mod_remove
import mod_remove_all
import mod_search
import mod_view
import json
import os
from mod_log import LOG
from mod_city import get_city_id


def get_dir():
    return os.path.dirname(os.path.realpath(__file__))

@LOG
def open_exist():
    with open(get_dir()+'\db_main.json', 'r', encoding='utf-8') as file:
        pb = json.loads(file.read())
    mod_view.display_all(pb)
    return pb

@LOG
def initial_database():
    temp = []
    print('Чтобы начать предлагаем сохранить первый контакт\n')
    pb = []
    rows = 1
    cols = 6
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Введите ID: ")))
                if temp[j] == '' or temp[j] == ' ':
                    print("ID является обязательным полем.")
                    return
            if j == 1:
                temp.append(str(input("Введите имя: "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    print("Имя является обязательным полем.")
                    return
            if j == 2:
                temp.append(str(input("Введите фамилию: ")))
            if j == 3:
                temp.append(str(input("Введите день рождения (дд/мм/гг): ")))
            if j == 4:
                temp.append(get_city_id(str(input("Город проживания: "))))
            if j == 5:
                temp.append(str(input("Введите номер телефона: ")))
    pb.append(temp)
    mod_view.display_all(pb)
    save_database(pb)
    return pb

@LOG
def save_database(pb):
    with open(get_dir()+'\db_main.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(pb))

@LOG
def start():
    os.system('cls' if os.name=='nt' else 'clear')
    print("\nБаза сотрудников компании\n")
    ch = 1
    if os.path.exists(get_dir()+'\db_main.json'):
        pb = open_exist()
    else:
        pb = initial_database()
    while ch in (1, 2, 3, 4, 5):
        ch = mod_menu.menu()
        if ch == 1:
            pb = mod_add.add_contact(pb)
        elif ch == 2:
            pb = mod_remove.remove_existing(pb)
        elif ch == 3:
            pb = mod_remove_all.delete_all(pb)
        elif ch == 4:
            d = mod_search.search_existing(pb)
            if d == -1:
                print("\nКонтакт не существует. Пожалуйста, попробуйте еще раз")
        elif ch == 5:
            mod_view.display_all(pb)
        else:
            print("\nДо свидания :)")