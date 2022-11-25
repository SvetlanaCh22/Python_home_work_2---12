import os
import mod_view
from mod_log import LOG
from mod_city import get_city_id

@LOG
def search_existing(pb):
    """ Эта функция ищет существующий контакт и отображает результат """
    try:
        choice = int(input("\nВведите критерии поиска\
        \n1. ID\n2. Имя\n3. Фамилия\n4. День рождения\n5. Город проживания\n6. Телефон\
        \nПожалуйста, введите: "))
    except ValueError:
        print('Пожалуйста, введите число от 1 до 6')
        return -1
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Пожалуйста, введите ID контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = str(input("Пожалуйста, введите имя контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        query = str(input("Пожалуйста, введите фамилию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query = str(input("Пожалуйста, введите день рождения (ТОЛЬКО в формате дд/мм/гггг)\
            контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    elif choice == 5:
        query = str(input("\nПожалуйста, введите город проживания: "))
        for i in range(len(pb)):
            if get_city_id(query) == pb[i][4]:
                check = i
                temp.append(pb[i])
    elif choice == 6:
        query = str(input("\nПожалуйста, введите номер телефона: "))
        for i in range(len(pb)):
            if query == pb[i][5]:
                check = i
                temp.append(pb[i])
    else:
        print("Неверные критерии поиска")
        return -1
    # возврат -1 означает, что поиск не увенчался успехом
    if check == -1:
        return -1
    # возвращение -1 указывает, что запрос не существует в каталоге
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        mod_view.display_all(temp)
        return check