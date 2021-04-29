print('Hello, World')

from lesson2_2.database import simpledb
db = Simpledb(‘recipes.txt’)
db.insert(‘relish’, ‘Pickled cucumber and sugar’)
print(db.select_one(‘relish’))