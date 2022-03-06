def add_to(a,b):
    return a+b
def mul(a,b):
    return a*b
def dev(a,b):
    print(f"c={a/b}")
def sub(a,b):
    return a-b

while True:
    print("1.For Addition\n2.For Substraction\n3.For multiplication\n4.For division\n5.For exit")
    q=int(input("Enter choice:-"))
    if q==1:
        e=int(input("Enter first no:-"))
        f=int(input("enter second no:-"))
        c=add_to(e,f)
        print (c)
    elif q==2:
         e=int(input("Enter first no:-"))
         f=int(input("enter second no:-"))
         c=sub(e,f)
         print(c)
    elif q==3:
         e=int(input("Enter first no:-"))
         f=int(input("enter second no:-"))
         c=mul(e,f)
         print(c)
    elif q==4:
         e=int(input("Enter first no:-"))
         f=int(input("enter second no:-"))
         c=dev(e,f)
    elif q==5:
        break
    else:
        print("wrong choice")
        continue



