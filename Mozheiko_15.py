def Decor(fun):
    def rebuild(arg):
        arg = str(arg).upper()
        fun(arg)
    return rebuild

@Decor
def hello(name):
    print(f'Привет, {name}!')
hello("Andrew")


#Это точно рабочий вариант без лишнего кода и издевательств над ним)))
def num_sum(num):
    if num !=0:
        return num%10 + num_sum(num//10)
    else:
        return 0
print('Сумма цифр числа:', num_sum(111111111111))
print('Сумма цифр числа:', num_sum(123))

#А дальше начинается издевательство
def weird_function(fun):
    def magic(arg):
        trick = []
        while arg > 0:
            trick.append(arg % 10)
            arg //= 10
        trick.reverse()
        arg = trick
        fun(arg)
    return magic

@weird_function
def sum_rec(num):
    print('Вот что декоратор "weird_function" сделал с введенным числом:', num)
    print(f"Сумма цифр числа: {sum(num)}")

sum_rec(123)
sum_rec(111111111111)