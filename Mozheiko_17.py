from time import sleep


class Company:

    levels = {1: 'Junior',
              2: 'Middle',
              3: 'Senior',
              4: 'Lead'}

    def __init__(self, index):
        self._index = index
        self._levels = self.levels[index]

    def _level_up(self):
        if self._index <= 3:
            self._index += 1
            self._levels = self.levels[self._index]
            print('Ты стал', self._levels)
        else:
            print('Ты уже Лид. Теперь пора открывать свою компанию!')

    def is_lead(self):
        if self._index == 4:
            print('Твой уровень: Lead')
        else:
            print('Пока что ты не лид. Ты', self._levels)


x = Company(1)
x.is_lead()


class Programmer(Company):

    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
        self.level = self.levels[level]

    def work(self):
        self._level_up()

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age} лет\n'
              f'Квалификация: {self._levels}')

    def knowledge_base(self):
        print('Зачем вставлять какой-то текст, если можно...\n...')
        sleep(1)
        print('Показать что-то стоящее?')
        sleep(1.5)
        print('https://clck.ru/Vmr3g')


z = Programmer('Drew', 26, 3)
z.work()
z.info()
z.work()
z.info()
z.knowledge_base()
