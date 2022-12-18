def decorator(function):
    def wrapper(arg):
        if type(arg) == int: print('Тип данных - число')
        elif type(arg) == str: print('Тип данных - строка')
        elif type(arg) == list: print('Тип данных - список')
        elif type(arg) == tuple: print('Тип данных - кортеж')
        else: print('Тип данных не число, строка, список или кортеж')
        function(arg)
    return wrapper

@decorator
def type_o_negative(data):
    if type(data) == str:
        z = 0
        for i in data:
            if i.isalpha(): z += 1
        print('Всего букв: ', z)
    elif type(data) == int:
        z = 0
        for i in str(data):
            if int(i) % 2 != 0:
                z += 1
        print('нечетных чисел: ', z)
    elif type(data) == list:
        nums = 0
        letters = 0
        for i in str(data):
            if i.isdigit(): nums += 1
            elif i.isalpha(): letters += 1
        print(f'Всего чисел: {nums}\nВсего букв: {letters}')
    elif type(data) == tuple:
        counter = 0
        for i in data:
            if type(i) != int:
                counter += len(i)
        print('Длина всех строк: ', counter)
