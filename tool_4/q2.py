# .Modify the question 1 and create 5 objects as s1,s2,s3,s4,s5. 
# Input data as required and calculate average cgpa marks.

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

s1=school("Bishop Bhaumik",1928024,"CSSE",9.22)
s2=school("kolp",1928329,"CSSE",7.64)
s3=school("XYZ",1928002,"CSSE",8.97)
s4=school("Trishit",1928004,"CSSE",9.00)
s5=school("Sourav",192098,"CSSE",9.212)

sum=0

ci=[s1.cgpa,s2.cgpa,s3.cgpa,s4.cgpa,s5.cgpa]
for i in ci:
    sum=sum+i 
avg=sum/5
print(f"the average is {avg}")