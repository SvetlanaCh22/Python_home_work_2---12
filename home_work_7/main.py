import mod_init
import mod_menu
import mod_add
import mod_remove
import mod_remove_all
import mod_search
import mod_view
import os

# Код основной функции
clear = lambda: os.system('cls')
clear()
print("\nДобро пожаловать в телефонный справочник.\n")
ch = 1
dir_path = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(dir_path+'\spravochnik.json'):
    pb = mod_init.open_exist()
else:
    pb = mod_init.initial_phonebook()
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
            print("Контакт не существует. Пожалуйста, попробуйте еще раз")
    elif ch == 5:
        mod_view.display_all(pb)
    else:
        print("До свидания :)")
