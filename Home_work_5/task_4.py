#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def incodeRLE(exp):
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


def decodeRLE(exp):
    decode = ''
    count = ''
    for char in exp:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


#origin ='kkkiiggwwwwwwwl'
# print(incodeRLE(origin))
#convert = incodeRLE(origin)
# print(decodeRLE(convert))


# _________________________________________________________________________
# Если без функций

origin = 'fffffffeerkll'
incoding = ""
i = 0
while i < len(origin):
    count = 1
    while i + 1 < len(origin) and origin[i] == origin[i + 1]:
        count = count + 1
        i = i + 1
    incoding += str(count) + origin[i]
    i = i + 1
print(incoding)

decode = ''
count = ''
for char in incoding:
    if char.isdigit():
        count += char
    else:
        decode += char * int(count)
        count = ''
print(decode)
