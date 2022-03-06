#not implemented error(Abstract method)

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('You have to define the method in child class')
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return f"the sound is barking"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return f"meao meao"
sp=Dog('Boony','pug')
print(sp.sound())
ci=Cat("sui","me")
print(ci.sound())
