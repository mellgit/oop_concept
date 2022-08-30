"""

"""


class Person:
    def __init__(self, name, old) -> None:
        # для работы с __ - геттеры и сеттеры
        self.__name = name
        self.__old = old

    # арт.класса мб много, чтобы все не запоминать все геттеры и сеттеры, используют property
    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)


p = Person('anna', 20)
print(p.old)  # 20
p.old = 34
print(p.old, p.__dict__)  # 34 {'_Person__name': 'anna', '_Person__old': 34}

print()


#! Более правильная реализация, при помощи декораторов
"""
1 - над геттером - @property
2 - над сеттером - name_getattr.setter (пример: @old.setter)
3 - сеттер переименуем как геттер (одинаковые именя методов)
использовать только геттер, через объект класса,
а присваивания или взятие значения определяется автоматом
"""

class Person:
    def __init__(self, name, old) -> None:
        # для работы с __ - геттеры и сетторы
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    # дополнительно deleter
    @old.deleter
    def old(self):
        del self.__old

    

p = Person('anna', 20)
print(p.old)  # 20
p.old = 34
# 34 {'_Person__name': 'anna', '_Person__old': 34}
print(p.old, p.__dict__)

del p.old
# AttributeError: 'Person' object has no attribute '_Person__old'
# ошибка, тк атр.класса был удален
print(p.old, p.__dict__)
