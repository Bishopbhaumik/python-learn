def grat(a,b):
    if a>b:
        return a
    return b

def gratest(a,b,c):
    bigger=grat(a,b)
    return grat(bigger,c)               

num1=int(input("ENTER NUMBER 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
c=gratest(num1,num2,num3)
print(f"The gratest no is {c}")