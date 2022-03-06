def lop(a):
    for i in range(1,a+1):
        if(i%2==0):
            yield(i)

 
for n in lop(10):
    print(n)