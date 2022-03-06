#print average of n number of list 

ec=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]

n=int(input("enter the number of list inside the list:"))
p=int(input("enter the length of inner list:"))
ct=[]
for i in range(n):
 ct.append(list([int(input())for j in range(0,p)]))
 print('\n')
print(ec([1,2,3],[3,5,7],[6,1,9]))
print(ct)
print(ec(*ct))