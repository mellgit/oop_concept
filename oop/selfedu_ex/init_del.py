"""
__init__(self) - инициализатор объекта класса
вызывается сразу после создания экземпляра класса

__del__(self) - финализатор класса
вызывается перед удалением эк.класса

Сборщик мусора удаляет в тот момент, когда пропадают все внешние ссылки на объект
"""


class Point:
    color = 'red'
    circle = 2

    # def __init__(self, x=0, y=0) -> None: - значения по умолчанию
    def __init__(self, x, y) -> None:
        print('call __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print(f'delete ex.class {str(self)}')

    def set_coords(self, x, y):  
        self.x = x
        self.y = y
        

    def get_coords(self):
        return (self.x, self.y)


a = Point(1, 2)  # call __init__
print(a.__dict__)  # {'x': 1, 'y': 2}
