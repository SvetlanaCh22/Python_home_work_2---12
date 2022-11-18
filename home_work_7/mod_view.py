# эта функция отображает все содержимое телефонной книги pb
def display_all(pb):
    if not pb:
# если функция отображения вызывается после удаления всех контактов, то len будет 0
# А без этого условия выдаст ошибку
        print("Список пуст")
    else:
        print("")
        max_len = max([len(str(e)) for r in pb for e in r])
        for row in pb:
            print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))