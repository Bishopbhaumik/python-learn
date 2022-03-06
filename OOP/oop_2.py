class ball:
    def fun(self):
       a=int(input("Enter the value:"))
       b=0 
       sum=0 
       s=[None]*a
       for val in range(0,a):
           b=int(input("enter array:"))
           s[val]=b
           sum= sum+s[val]
           print("SUM OF THE ARRAY ELEMENTS:",sum)
       for val in range(0,a):
           print(s[val]) 
    

import math
# obj = ball() 
# obj.fun
print(math.gcd(15,25,125))

