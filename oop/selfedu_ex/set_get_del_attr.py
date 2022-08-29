"""
Если необходимо изменить атр.класса (MAX_COORD), стоит использовать classmethod

__setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
__getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
__getattr__(self, item) - автоматически вызывается при получении несуществующего свойсва item класса
__delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно: существует оно или нет)

"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


a = Point(10,20)
a.set_bound(-100)
print(a.__dict__)  # {'x': 10, 'y': 20}
print(Point.__dict__)  # 'MIN_COORD': -100,
print()



class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    # возвращает свойства класса
    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)

    # присвоение значения
    def __setattr__(self, key, value) -> None:
        print('__setattr__')
        # object.__setattr__(self, key, value)
        return False

    # проверка на существования атр.класса
    def __getattr__(self, item):
        print(f'__getattr__ {item}')
    
    # при удалении атр.класса
    def __delattr__(self, item):
        print(f'__delattr__ {item}')
        object.__delattr__(self, item)




a = Point(10, 20)
b = a.x
print(b)
"""
Output: 
__setattr__ - два одинаковых из за строчек 60 и 61
__setattr__
__getattribute__
10
"""