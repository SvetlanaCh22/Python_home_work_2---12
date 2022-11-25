from mod_log import LOG
import os

@LOG
def menu():
    """ Главное меню """
    print("\n\t\t\tМеню программы\n", flush=False)
    print("1. Добавить новый контакт")
    print("2. Удалить существующий контакт")
    print("3. Удалить все контакты")
    print("4. Поиск контакта")
    print("5. Показать все контакты")
    print("6. Выход из базы данных")
    try:
        choice = int(input("Введите пункт меню: "))
    except:
        choice = 5
    os.system('cls' if os.name=='nt' else 'clear')
    return choice