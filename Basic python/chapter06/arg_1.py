def totasl(num,*args):
    ti=0
    for i in args:
        ti=ti+i
    print(num+ti)
    return ti

print(totasl(2,3,4,5,6,6,7,8,9))
num=[2,3,4]
print(totasl(*num))
