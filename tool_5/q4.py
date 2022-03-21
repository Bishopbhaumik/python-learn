#Create a child class Chess that will inherit all of the variables and methods of the Indogame class

class Indgames():
    def __init__(self,name):
        self.name=name
    def first(self):
        print("There are many indoor games")

class chess(Indgames):
    def __init__(self,name,age):
       super().__init__(name)
       self.age=age
    def second(self):
        print("chess is one of them")
        
        
obj=chess("Ram",13)
obj.first()
obj.second()
print(obj.name)
print(obj.age)