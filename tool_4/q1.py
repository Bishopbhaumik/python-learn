# 1.Write a program in python using the concept of object. 
# The class contain (name, roll, branch, cgpa).
# Create a object student. Input date as required and display them.

class school:
    def __init__(self,name,roll,branch,cgpa):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.cgpa=cgpa
    def show(self):
        print(f"name:{self.name}")
        print(f"roll:{self.roll}")
        print(f"branch:{self.branch}")
        print(f"CGPA:{self.cgpa}")
        
student=school("Bishop Bhaumik",1928024,"CSSE",9.22)
student.show()