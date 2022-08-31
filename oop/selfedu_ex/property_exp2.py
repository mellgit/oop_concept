

from string import ascii_letters


class Person:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()


    def __init__(self, fio, old, ps, weight) -> None:
        # проверка, что все входные данные корректны
        self.verify_fio(fio) # если не будет ошибок, программа продолжит работу, иначе Traceback
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        # вариант лучше
        self.__fio = fio.split()
        self.old = old # в таком случае сразу буду вызваны сеттеры
        self.passport = ps
        self.weight = weight
        
        

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('last name must be a string ')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('wrong format')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) <1:
                raise TypeError('must be at least one character')
            if len(s.strip(letters)) != 0:
                raise TypeError('only letters, symbols and hyphens can be used')


    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('age must be a number in the range [14;120]')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('weight must be a number 20 or more')


    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('passport must be a string')
        
        s = ps.split()
        if len(s) != 2 or len(s[0]) !=  4 or len(s[1]) != 6:
            raise TypeError('invalid passport format')
        
        for p in s:
            if not p.isdigit():
                raise TypeError('series and passport number must be numbers')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport

    



p = Person('Иванов Иван Иванович', 30, '1234 567890', 80.0) # True
# p = Person('ИвановИван Иванович', 30, '1234 567890',80.0)  # TypeError: wrong format

p.old = 100
p.passport = '2345 345655'
p.weight = 70.0

print(p.__dict__)
# {'_Person__fio': ['Иванов', 'Иван', 'Иванович'], '_Person__old': 100, '_Person__passport': '2345 345655', '_Person__weight': 70.0}
