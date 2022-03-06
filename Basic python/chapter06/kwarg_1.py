 
def aty(**kwargs):
     for i,v in kwargs.items():
         print(f"{i}:{v}")
    
aty(first='Bishop',last='Bhaumik',Age=19)
#PADK
n=int(input("enter range:"))
li=[(int(input("enter value:"))) for i in range(1,n+1)]
print(f"the list is :{li}")
print(f"after mapping the square:---------------->")
print(list(map(lambda a:a**2,li)))
print("using the enamurate function:-")
for tp,mp in enumerate(li):
    print(f"{tp+1}:{mp}")



