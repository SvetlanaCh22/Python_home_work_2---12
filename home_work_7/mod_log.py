import mod_init
from datetime import datetime

# идея заимствована у Данила Самодурова, с доработкой под возвращаемые значения функции
def LOG(func):
    def wrapper(*args):
        ret = func(*args)
        with open(mod_init.get_dir()+'\log.txt', 'a', encoding='utf-8') as log:
            log.write(f'{datetime.now()}    {func.__name__}    ({func.__doc__})\n')
        return ret    
    return wrapper