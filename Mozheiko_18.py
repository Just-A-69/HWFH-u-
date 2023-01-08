import sqlite3

fsa = [['Andrew', 'Mozheiko', 27], ['Jonny', 'Travis', 42], ['Isaak', 'Asimov', 72]]

base = sqlite3.connect('names.db')
cursor = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS fio(name TEXT, surname TEXT, age INTEGER)')
cursor.executemany('INSERT INTO fio VALUES(?, ?, ?)', fsa)
base.commit()

base.execute('CREATE TABLE IF NOT EXISTS animals(animal TEXT, age INTEGER)')
cursor.execute('''INSERT INTO animals(animal, age) VALUES('Zebra', 19)''')
cursor.execute('''INSERT INTO animals(animal, age) VALUES('Axolotl', 3)''')
cursor.execute('''INSERT INTO animals(animal, age) VALUES('Elephant', 52)''')
cursor.execute('''INSERT INTO animals(animal, age) VALUES('Bat', 1)''')
base.commit()
