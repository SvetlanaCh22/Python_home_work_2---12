import os
import json
import mod_init
from mod_log import LOG

@LOG
def open_city_exist():
    with open(mod_init.get_dir()+'\db_city.json', 'r', encoding='utf-8') as file:
        cb = json.loads(file.read())
    return cb

@LOG
def save_city_database(cb):
    with open(mod_init.get_dir()+'\db_city.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(cb))

@LOG
def add_city_id(cb, city, row_id):
    dip = [] # создаем новый город в базе
    dip.append(row_id)
    dip.append(city)
    cb.append(dip)
    save_city_database(cb)

@LOG
def get_city_id(city):
    """Возвращает ID города из базы городов по имени"""
    if os.path.exists(mod_init.get_dir()+'\db_city.json'):
        cb = open_city_exist()
        row_id = str(len(cb))
        for row in cb:
            if row[1]==city:
                return str(row[0])
        add_city_id(cb, city, row_id)
        return row_id
    else:
        cb = [] # создаем пустую базу данных городов
        row_id = '0'
        add_city_id(cb, city, row_id)
        return '0'

@LOG
def get_city(id):
    """Возвращает имя города по его ID из базы данных"""
    if os.path.exists(mod_init.get_dir()+'\db_city.json'):
        cb = open_city_exist()
        for row in cb:
            if str(row[0])==str(id):
                return str(row[1])
        return 'неизвестный город'
    else:
        return 'неизвестный город'