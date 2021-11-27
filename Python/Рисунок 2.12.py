class Animal:
    defaultVoice = "AAAAA"  # статичний атрибут

    def __init__(self, name, origin):
        self.animal_name = name  # динамічний атрибут
        self.animal_origin = origin


myAnimal = Animal("Elephant", "Africa")
print(myAnimal.animal_name + " comes from " + myAnimal.animal_origin)
print("It says: " + Animal.defaultVoice)
