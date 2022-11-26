import os
from datetime import datetime

def get_dir():
    return os.path.dirname(os.path.realpath(__file__))

# идея заимствована у Данила Самодурова, с доработкой под возвращаемые значения функции
def LOG(func):
    def wrapper(*args):
        ret = func(*args)
        with open(get_dir()+'\\'+'botlog.txt', 'a', encoding='utf-8') as log:
            log.write(f'{datetime.now()} - {func.__name__}    ({func.__doc__})\n')
        return ret    
    return wrapper

def print_LOG(text):
    with open(get_dir()+'\\'+'botlog.txt', 'a', encoding='utf-8') as log:
        log.write(f'{datetime.now()} - {text}\n')
    return