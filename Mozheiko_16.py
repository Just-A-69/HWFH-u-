class Main_Function:
    def first_method(self, a):
        if type(a) == str:
            gl = []
            sg = []
            for i in list(a.lower()):
                if i.isalpha() and i in 'eyuioa':
                    gl.append(i)
                elif i.isalpha() and i in 'qwrtpsdfghjklzxcvbnm':
                    sg.append(i)
                else:
                    continue
            if self.dlinnomer(gl) * self.dlinnomer(sg) <= self.dlinnomer(a):
                print('Произведение гласных и согласных меньше или равно длине строки.\nВывожу все гласные:', *gl)
            elif self.dlinnomer(gl) * self.dlinnomer(sg) > self.dlinnomer(a):
                print('Произведение гласных и согласных больше длины строки.\nВывожу все согласные:', *sg)
        elif type(a) == int:
            dlina = self.dlinnomer(a)
            if a < 0:
                dlina = self.dlinnomer(a) - 1
                a = a * -1
            num = list(str(a))
            che = 0
            for i in num:
                if int(i) % 2 == 0:
                    che += int(i)
            print('Произведение суммы четных цифр на длину числа:', che * dlina)
        elif type(a) == float:
            dlina = self.dlinnomer(a) - 1
            if a < 0:
                dlina = self.dlinnomer(a) - 2
                a = a * -1
            num = list(str(a))
            che = 0
            for i in num:
                if i.isdigit():
                    if int(i) % 2 == 0:
                        che += int(i)
            print('Произведение суммы четных цифр на длину числа:', che * dlina)

    def dlinnomer(self, a):
        return len(str(a))


a = Main_Function()
a.first_method('AaBbCcDdEe!=_$*#')
a.first_method(987)
a.first_method(-987)
a.first_method(9.87)
a.first_method(-98.7)