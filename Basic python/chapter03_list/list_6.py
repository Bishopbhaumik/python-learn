matrix=[[1,2,3],[4,5,6],[7,8,9]]
for sub in matrix:
    print(sub)

print("Printing distinct element:---------------------------->")

for sub in matrix:
    for i in sub:
        print(i)

nu=list(range(1,23))
print(nu)

def neg(l):
    a=[]
    for i in nu:
        a.append(-i)
    return a

pi=neg(nu)
print(f"the negetive of the list is {pi}")
