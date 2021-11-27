class Animal:
    defaultVoice = "AAAAA"  # статичний атрибут

    def __new__(cls, *args, **kwargs):  # функція створення нового об`єкту
        print("This message from __new__ block")
        return object.__new__(cls)  # використання базового методу класу object

    def __init__(self, name, origin):  # функція ініціалізації
        print("This message from __init__ block")
        self.animal_name = name  # динамічний атрибут
        self.animal_origin = origin




myAnimal = Animal("Elephant", "Africa")
