import mod_init
from mod_log import LOG

@LOG
def remove_existing(pb):
    """ Эта функция предназначена для удаления сведений о контакте из существующей телефонной книги. """
    query = str(input("\nПожалуйста, введите имя контакта, который вы хотите удалить: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            # Функция pop удалит запись с индексом i.
            print("\nЭтот запрос был удален")
            # После удаления вернем измененную телефонную книгу  
            mod_init.save_database(pb)
            return pb
    if temp == 0:
        print("Извините, вы ввели неверный запрос.\
    Пожалуйста, перепроверьте и повторите попытку позже.")
        return pb