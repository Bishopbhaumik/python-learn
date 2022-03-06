i=1
n=int(input("enter a number:"))
total=0
toa=0
for i in range (1,n):
    total=total+i

print(f"The sum of n number of inputs are :{total}")
#now sum of even numbers uptonthe number
for i in range (1,n):
    if i%2==0:
        toa=toa+i
    else:
        pass
print(f"Total sum of even numbers upto the number is :{toa}")
        