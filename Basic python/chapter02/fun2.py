def my_sum(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    print(f"wrong input")


print(my_sum(1,2,3,4,5,8.9,7.8,'Bishop'))

l1=[1,3,5,7]
l2=[2,4,6,8,]
l3=[1,2,3,5,7,9]

print(all([num%2==0 for num in l2]))
print(any([num%2==0 for num in l3]))
