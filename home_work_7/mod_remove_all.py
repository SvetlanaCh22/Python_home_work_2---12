import mod_init
from mod_log import LOG

@LOG
def delete_all(pb):
    """ Эта функция удалит все записи в базе данных pb и вернет пустую базу """
    choice = input("Уверены(Да/Нет): ")
    if choice=="Да":
        pb.clear()
        mod_init.save_database(pb)
        print("\nБаза данных очищена")
    return pb