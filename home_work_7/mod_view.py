from mod_log import LOG
from mod_city import get_city

@LOG
def display_all(pb):
    """ эта функция отображает все содержимое базы данных pb """
    if not pb:
        # если функция отображения вызывается после удаления всех контактов, то len будет 0
        # А без этого условия выдаст ошибку
        print("База данных пуста")
    else:
        print("")
        max_len = max([len(e) for r in pb for e in r])
        for row in pb:
            row1 = []
            for col in row:
                row1.append(col)
            row1[4] = get_city(row1[4])
            print(*list(map('{{:>{length}}}'.format(length=max_len).format, row1)))

@LOG
def check_id(pb, id):
    """ проверка существования id """
    if not pb:
        print("База данных пуста")
        return True
    else:
        for row in pb:
            if row[0]==id:
                return False
        return True