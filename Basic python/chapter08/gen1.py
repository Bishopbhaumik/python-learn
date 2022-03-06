#creating generator
# 10 ,1, t0 10

def nu(n):
    for i in range(1,n+1):
        # print(i)
        yield(i)#creating generator


print(nu(10))
# for n in nu(10):
#     print(n)
number=nu(10)
ni=list(nu(10))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
for i in ni:
    print(i)