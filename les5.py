import json


class Pet:
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    @classmethod
    def from_str(cls, oops:str):
        name, breed = map(str.strip, oops.split(':'))
        return cls(name, breed)


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
        return "Порода: {0} - {1}".format(self.name, self.breed)
    

issubclass(Dog, Pet)

dog = ExDog("Джек", "Питбуль")
dog2 = ExDog.from_str("Штрудель:Пудель")
cat = Cat("Маркиз", "Сиам")
dog3 = Dog.from_str("    Данте                :         Доберман         ")

print(dog.get_breed())
print(dog.say())
print("-----------------")
print(dog2.get_breed())
print(dog2.say())
print("-----------------")
print(dog3.get_breed())
print(dog3.say())
print("-----------------")

print(cat.get_breed())
print(cat.say())
