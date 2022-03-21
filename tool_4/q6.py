# Write a python program to define a class Number with appropriate data
# members and member functions to input n number of integers and swap 
# the biggest and smallest elements. Use member functions read(), 
# swap() and display().

class number:
  a=[]
  def read(self):
    self.a=list(map(int,input().split()))
  def display(self):
    print(self.a)
  def swap(self):
    i=j=0
    while(i<len(self.a)):
      if self.a[i]==max(self.a):
        break
      i+=1
    while(j<len(self.a)):
      if self.a[j]==min(self.a):
        break
      j+=1
    self.a[i],self.a[j]=self.a[j],self.a[i]


n=number()
n.read()
n.display()
n.swap()
n.display()