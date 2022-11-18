import mod_init
def delete_all(pb):
# Эта функция просто удалит все записи в телефонной книге pb.
# Он вернет пустую телефонную книгу после очистки
    pb.clear()
    mod_init.save_phonebook(pb)
    return pb