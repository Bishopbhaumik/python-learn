class Person:
    def __init__(self,first,last,age,to):
        self.first=first
        self.last=last
        self.age=age
        self.total=to
        self.si=to+self.total
    def show_data(self):
        print(f"the name is :--->{self.first} {self.last}")
        print(f"Age is :{self.age}")
        print(f"total marks:=====>{self.total}")

a=Person("Bishop",'Bhaumik',20,100)
print(a.age)
print(a.first)
print(a.last)
a.show_data()