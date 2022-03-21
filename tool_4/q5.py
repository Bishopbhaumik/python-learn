# 5.Write a python program to input and
# display the details of n number of  students having roll, 
# name and cgpa as data members. Also display the name  of the 
# student having lowest cgpa.

class school:
    def __init__(self,name,roll,cgpa):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa
    def show(self):
        print(f"name:{self.name}")
        print(f"roll:{self.roll}")
        print(f"CGPA:{self.cgpa}")

        
  

n=int(input("enter number of students:"))        
ci=[school(input("enter name:"),input("enter roll:"),float(input("enter cgpa:"))) for i in range(1,n+1)]
print(f"Output=================>\n")
for i in ci:
    i.show()
    # k=i.su(ci)
  
# po=[i.cgpa for i in ci]
# print(f"the lowest cgpa is {min(po).}")
minio=ci[0].cgpa
cp=0
for i in ci:
    if i.cgpa<minio:
        minio=i.cgpa
        cp=i

print(f"The lowest cgpa is {cp.name}")