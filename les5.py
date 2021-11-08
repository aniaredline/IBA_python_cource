import json


class Pet:
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    def get_breed(self):
        return self.breed


class Dog(Pet):
    def say(self):
        return f"{self.name}: waw"


class Cat(Pet):
    def say(self):
        return f"{self.name}: meow"



class ExportJSON:
    def to_json(self):
        return json.dumps({"name": self.name, "breed": self.breed})


class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "порода: {0} - {1}".format(self.name, self.breed)
    

issubclass(Dog, Pet)

dog = ExDog("Джек", "Питбуль")
cat = Cat("Мурзик", "Сиам")

print(dog.get_breed())
print(dog.say())

print(cat.get_breed())
print(cat.say())
