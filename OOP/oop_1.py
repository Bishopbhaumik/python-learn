# class Test: 
      
#     # A sample method  
#     def fun(self): 
#         print("Hello") 
# # Driver code         
# obj = Test() 
# obj.fun()
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
    def su(num):
      so=0
      for i in num:
          so=so+i.total
      return(so/len(num))

a=Person("Bishop",'Bhaumik',20,100)
print(a.age)
print(a.first)
print(a.last)
a.show_data()
n=int(input("enter number of bjects to be created:"))
ci=[Person(input("enter first name:"),input("enter last name:"),int(input("enter age:")),int(input("enter total marks:")))for i in range(1,n+1)]
print(f"OUTPUT=================================>\n")
for i in ci:
    i.show_data()
    # k=i.su(ci)
k=Person.su(ci)
print(f"the average mark of the class is :{k}")