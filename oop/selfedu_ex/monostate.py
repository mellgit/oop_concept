"""
Паттерн "Моносостояние"
Предначначен для равенства свойств у разных объектов одного класса
"""

class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    # при инициализации нового объекта, коллекция __dict__ будет ссылаться на один и тот же словарь
    def __init__(self) -> None:
        self.__dict__  = self.__shared_attrs

    
th1 = ThreadData()
th2 = ThreadData()
print(th1.__dict__)  # {'name': 'thread_1', 'data': {}, 'id': 1}
print(th2.__dict__)  # {'name': 'thread_1', 'data': {}, 'id': 1}

# свойства заменяются в всех объектах класса
# заменил один - заменил все
th2.id = 5

print(th1.__dict__)  # {'name': 'thread_1', 'data': {}, 'id': 5}
print(th2.__dict__)  # {'name': 'thread_1', 'data': {}, 'id': 5}

# создал один новый эк.класса - создал его во всех объектах 
th1.attr_new = 'new_attr'


print(th1.__dict__)
# {'name': 'thread_1', 'data': {}, 'id': 5, 'attr_new': 'new_attr'}
print(th2.__dict__)
# {'name': 'thread_1', 'data': {}, 'id': 5, 'attr_new': 'new_attr'}
