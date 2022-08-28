"""
__new__(cls) - вызывается перед созданим объекта класса
cls - ссылкается на текущий эк.класса (имеется ввиду Point)
self - на создаваемый эк.класса
"""
"""
Для чего нужен __new__()
Паттерн Singleton
чтобы был создан только один эк.класса, 
если будет создан второй, то он будет ссылаться на первый
(приммер, класс DataBase)
"""



class DataBase:
    # ссылка на эк.класса, для проверки состояния класса, те что класс один
    __instance = None 

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # если создается самый первый эк.класса
        
        return cls.__instance # если эк.класса уже создан

    def __del__(self):
        # если объект класса будет удален сборщиком,
        # то атр __instance снова будет None
        DataBase.__instance = None

    def __init__(self, user, port, psw) -> None:
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connection with DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print(f'disconnect DB')

    def read(self):
        return f'data from DB'

    def write(self, data):
        print(f'write in DB {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root3', '5678', 40)
# адресса равны, тк db ссылается на db2, 
# а не создается еще один объект db2
print(f'{hex(id(db))}: {hex(id(db2))}')  # 0x7f27f86dcd90: 0x7f27f86dcd90

# немного неправильно работает, тк сохраняются последния данные,
# потому что каждый раз, при создании нового объекта,
# вызывается __init__() метод
# это может решить метод __call__()
db.connect()  # connection with DB: root3, 40, 5678
db2.connect()  # connection with DB: root3, 40, 5678




class Point:

    def __new__(cls, *args, **kwargs):
        """
        new - должен возвращать адрес нового созданного объекта,
        иначе эк.класса Point не будет создан
        args, kwargs - обязательны
        """
        print(f'call __new__ for {str(cls)}')
        
        # ссылка на базовый класс и из базового класса, 
        # вызывается точно такой же метод __new__,
        # с ссылкой на текущий класс Point
        return super().__new__(cls) 

    def __init__(self, x=0, y=0) -> None:
        print(f'call __init__ for {str(self)}')

        self.x = x
        self.y = y


# a = Point(1, 2)  # call __new__ for <class '__main__.Point'>
# print(a)  # None

print()
# call __new__ for <class '__main__.Point'>
# call __init__ for <__main__.Point object at 0x7ff47064e9a0>
a = Point(1, 2)
print(a)  # <__main__.Point object at 0x7ff47064e9a0>

