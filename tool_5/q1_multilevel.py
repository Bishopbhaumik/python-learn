class Base1:
    def first(self):
        print("First base class")

class derive1(Base1):
        def second(self):
             print("second base class")

class Derived(derive1):
        def der(self):
           print("First derived class")
           
           
           
obj=Derived()
obj.first()
obj.second()
obj.der()