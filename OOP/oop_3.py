
class Person:
    oy=0
    si=0
    def __init__(self,first,last,age,to):
        Person.oy+=1
        self.first=first
        self.last=last
        self.age=age
        self.total=to
    def show_data(self):
        print(f"the name is :--->{self.first} {self.last}")
        print(f"Age is :{self.age}")
        print(f"total marks:=====>{self.total}")
    @classmethod
    def fromst(cls,string):
        first,last,age,toal=string.split(',')
        return cls(first,last,age,toal)
    @classmethod
    def count_inst(cls):
        return f"You have created {cls.oy} instances of {cls.__name__}"

    def above(self):
        return self.age>18
    def su(num):
      so=0
      for i in num:
          so=so+i.total
      return(so/len(num))
    @staticmethod
    def pil():
        print("Bishop Bhaumik")

print(Person.pil())
a=Person("Bishop",'Bhaumik',20,100)
a1=Person.fromst("Sai,Pallavi,24,98")
print(Person.count_inst())
print(a.above())
j=0
n=int(input("enter number of bjects to be created:"))
ci=[Person(input("enter first name:"),input("enter last name:"),int(input("enter age:")),int(input("enter total marks:")))for i in range(1,n+1)]
for i in (ci):
    j+=1
    print(f"{j} no student::--->")
    i.show_data()
    print("\n")

print(Person.count_inst())
k=Person.su(ci)
print(f"the average mark of the class is :{k}")
