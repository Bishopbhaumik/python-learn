# 4.Write a python program  to define a class Rectangle having data member: length and breadth; 
# to calculate the area and perimeter of the rectangle. 
# Use member functions to read, calculate and display.

class rectangle():
    def read(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
      return 2*(self.length+self.breadth)


a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj = rectangle().read(a,b)
print("Area of rectangle:",obj.area(a,b))
print("Perimeter of rectangle is:",obj.perimeter())
