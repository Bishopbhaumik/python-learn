class Base1:
    def first(self):
        print("First base class")

class Base2:
        def second(self):
             print("second base class")

class Derived(Base1, Base2):
        def der(self):
           print("First derived class")
           
           
obj=Derived()
obj.first()
obj.second()
obj.der()