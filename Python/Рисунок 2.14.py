class Animal:
    defaultVoice = "AAAAA"  # статичний атрибут

    def __new__(cls, *args, **kwargs):  # функція створення нового об`єкту
        print("This message from __new__ block")
        return object.__new__(cls)  # використання базового методу класу object

    def __init__(self, name, origin):  # функція ініціалізації
        print("This message from __init__ block")
        self.animal_name = name  # динамічний атрибут
        self.animal_origin = origin

    @staticmethod
    def make_animal_to_say(phrase):
        print(phrase + " is said with voice: " + Animal.defaultVoice)

    @classmethod
    def change_default_voice(cls, new_voice):
        cls.defaultVoice = new_voice

    def print_animal_info(self):
        print(self.animal_name + " comes from " + self.animal_origin)


myAnimal = Animal("Elephant", "Africa")
myAnimal.print_animal_info()

print("Animal common voice before change")
Animal.make_animal_to_say("Hi!")
Animal.change_default_voice("BBBBBBBB")

print("Animal common voice after change")
Animal.make_animal_to_say("Hi!")
