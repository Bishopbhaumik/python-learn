def power(t,p,*args):
    ui=[i**t for i in range(p)]
    return ui


n=int(input("enter length of the list:"))
t=int(input("enter the value to the power:"))
l=[i for i in range(1,n+1)]
p=len(l)
if(len(l)==0):
    print("empty list")
else:
    print("not empty")
    print(power(t,p,*l))

