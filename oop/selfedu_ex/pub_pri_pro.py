"""
Механизм инкапсуляции

public - без подчеркиваний, публичное свойства
private - _, служит для обращения внутри класса и во всех его дочерних классах
protected - __, для обращения только внутри класса

сетторы и гетторы - интерфейсные методы, чтобы правильно обращаться в атр.класса,
только через них, а не на прямую!!!

from accessify import private, protected - при помощи этих методов
можно защитить приватные свойства класса 
(более надежная защита, чем __ (обратиться через кодовое имя не получится))
"""

class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)

    # сеттор
    def set_coord(self, x, y):

        # проверка на тип данных
        # if type(x) in (int, float) and type(y) in (int, float):
        # более правильная проверка
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('coordinate must be a number')

    # геттор
    def get_coord(self):
        return self.__x, self.__y

a = Point(1,2)
# print(a.__x, a.__y) # обратиться не получится
# print(a._x, a._y)  # обратиться получится, но так не стоит использовать

a.set_coord(10,20)
print(a.get_coord())  # (10, 20)

# '_Point__x', '_Point__y' - кодовые имена, по которым можно обратиться к
# приватным свойствам
# print(dir(a))
# print(a.__x) # AttributeError: 'Point' object has no attribute '__x'
print(a._Point__x)  # 10, так делать крайне не рекомендуется 
