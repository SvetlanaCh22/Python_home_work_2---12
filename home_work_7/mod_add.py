import os
import mod_init
from mod_city import get_city_id
from mod_view import check_id
from mod_log import LOG

@LOG
def add_contact(pb):
    """ Функция добавления контактов """
    """ добавим еще один список в уже существующий список """
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            id = str(input("Введите ID*: "))
            if check_id(pb, id):
                dip.append(id)
            else:
                print("\nТакой ID уже существует")
                return pb          
        if i == 1:
            dip.append(str(input("Введите имя: ")) )
        if i == 2:
            dip.append(str(input("Введите фамилию: ")))
        if i == 3:
            dip.append(str(input("Введите день рождения (дд/мм/гг): ")))
        if i == 4:
            dip.append(get_city_id(str(input("Город проживания: "))))
        if i == 5:
            dip.append(str(input("Введите номер телефона: ")))
    pb.append(dip)
    mod_init.save_database(pb)
    os.system('cls' if os.name=='nt' else 'clear')
    print("Сотрудник добавлен в базу данных")
    return pb