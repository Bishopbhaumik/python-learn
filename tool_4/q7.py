class StudentData:
    def _init_(self,name,roll,branch,cgpa) -> None:
        self.name = name
        self.roll = roll
        self.branch = branch
        self.cgpa = cgpa
    def display(self) -> None:
        print(f"Answer : {self.name} with the roll number of {self.roll} belongs to {self.branch} branch and carries a cgpa of {self.cgpa}\n")

s1,s2,s3,s4,s5 = StudentData("aleena",4,"CSE",9.0), StudentData("Nidhi",9,"CSSE",9.0),StudentData("Chavvi",19,"CSE",8.0),StudentData("Riya",18,"IT",8.8),StudentData("Sanji",49,"CSE",7.0)


def cgpaAverage(s = []):
    cgpa = 0
    for i in range(0,5):
        cgpa += s[i].cgpa 
    cgpa = cgpa // 5
    for i in range(0,5):
        if cgpa < s[i].cgpa:
            print(f"{s[i].name} has a cgpa higher than the average")
objects = list()
objects.append(s1)
objects.append(s2)
objects.append(s3)
objects.append(s4)
objects.append(s5)
cgpaAverage(objects)