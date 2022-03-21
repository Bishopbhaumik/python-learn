# 8.Write a program in python using the concept of object. 
# Create a class rectangle with attribute (length, breath).
# Calculate area, perimeter of the rectangle.

class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
      return 2*(self.length+self.breadth)


a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj = rectangle(a,b)
print("Area of rectangle:",obj.area())
print("Perimeter of rectangle is:",obj.perimeter())