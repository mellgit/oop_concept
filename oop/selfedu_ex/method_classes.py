"""
Методы класса, параметр self
"""

class Point:
    color = 'red'
    circle = 2

    #  1 способ передачи параметров в метод
    def set_coords(self, x, y): # self - ссылка на экземпляр класса
        self.x = x
        self.y = y
        # call method <__main__.Point object at 0x7f1344395070>
        print(f"call method {str(self)}")

        # print(f'{self.x=}; {self.y=}')

    #  2 способ передачи параметров в метод
    def get_coords(self):
        return (self.x, self.y)

a = Point()
print(a.set_coords(1, 2))
print(a.__dict__) # свойства класса

print(a.get_coords())

# получение доступа к атрибутам класса через getattr
b = getattr(a, 'get_coords')
print(b())

