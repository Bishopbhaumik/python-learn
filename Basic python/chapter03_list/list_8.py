
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
print("After sorting=====>\n")
lst.sort()
print(lst) 

def ati(l):
    ti=[]
    for i in l:
        ti.append(i**2)
    return ti

s=ati(lst)
print ("\n After squaring the value======>\n")
print(s)