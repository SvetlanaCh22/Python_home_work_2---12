import mod_init

# Функция добавления контактов
def add_contact(pb):
# добавим еще один список в уже существующий список
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Введите ID*: ")))
        if i == 1:
            dip.append(str(input("Введите имя: "))) 
        if i == 2:
            dip.append(str(input("Введите фамилию: ")))
        if i == 3:
            dip.append(str(input("Введите день рождения (дд/мм/гг): ")))
        if i == 4:
            dip.append(str(input("Введите место работы: ")))
        if i == 5:
            dip.append(str(input("Введите номер телефона: ")))
    pb.append(dip)
    mod_init.save_phonebook(pb)
    return pb