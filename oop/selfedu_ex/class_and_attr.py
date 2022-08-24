class Point:
    """Класс координат точек"""
    # атрибуты класса
    color = 'red'
    circle = 2


def run():
    a = Point()
    print(a.__doc__)
    print(a.color)

    a.color = 'black' # можно менять вне класса
    print(a.color)

    setattr(Point, 'prop', 1) # добавление атрибута

    # проверка наличия атрибута
    # или hasattr(Point, 'color') => True
    print(getattr(Point, 'a', 'not found attr')) 

    delattr(Point, 'prop') # удаление атрибута

    print(Point.__dict__) # узнать все атрибуты класса
