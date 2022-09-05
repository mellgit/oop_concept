"""
Реализация дескриптора данных

non-data desctiptor - дескриптор не данных (only reed)
data descriptor - дескриптор данных (get, set, del)

"""

# non-data desctiptor
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


# data descriptor
class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('coordinate must be an integer')

    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


# p = Point3D(1,2,3)
# print(p.__dict__)
# __set__: _x = 1
# __set__: _y = 2
# __set__: _z = 3
# {'_x': 1, '_y': 2, '_z': 3}

p = Point3D(1, 2, 3)
p.xr = 5
print(p.xr, p.__dict__)  # 5 {'_x': 1, '_y': 2, '_z': 3, 'xr': 5}


 