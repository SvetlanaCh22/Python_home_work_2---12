#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def EncodeRLE(exp):
    incoding = ""
    i = 0
    while i < len(exp):
        count = 1
        while i + 1 < len(exp) and exp[i] == exp[i + 1]:
            count = count + 1
            i = i + 1
        incoding += str(count) + exp[i]
        i = i + 1
    return incoding


def DecodeRLE(exp):
    decode = ''
    count = ''
    for char in exp:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


origin ='kkkiiggwwwwwwwl'
print("Исходный вариант:", origin)
convert = EncodeRLE(origin)
print("Пакованный вариант:", convert)
print("Распакованный вариант:", DecodeRLE(convert))