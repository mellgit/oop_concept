"""
Декораторы @classmethod и @staticmethod
"""
"""
Если работа с арт класса - classmethod
работа с эк.класса - __init__ и тп
независивая(сервисная) ф-я - staticmethod (атр и эк тут не используют)
"""

class Vector:

    MIN_COORD = 0
    MAX_COORD = 150

    # работает исключительно с атр класса Vector
    # c self classmthod не работает
    # также classmethod можно использовать внутри других методов (например __init__)
    @classmethod
    def validate(cls, value):
        return cls.MIN_COORD <= value <= cls.MAX_COORD


    # независимая фу-я класса, не относящаяся ни к арт класса, ни к эк. класса
    # но его также можно вызывать и внутри других методов
    # ни self, ни cls для данного метода не нужны
    @staticmethod
    def norm2(x, y):
        return x**2 + y**2


    def __init__(self, x, y) -> None:

        self.x = self.y = 0
        
        # if Vector.validate(x) and Vector.validate(y): - можно записывать через имя класса
        # но self удобнее, если вдруг изменится имя класса        
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        # Vector.norm2(self.x, self.y) можно так, но снова self удобнее
        print(self.norm2(self.x, self.y))


    def get_coord(self):
        return self.x, self.y


v = Vector(1,2)
res = v.get_coord()
print(f'{res}')  # (1, 2)
print(Vector.validate(5)) # True
print(Vector.norm2(4,5)) # 41