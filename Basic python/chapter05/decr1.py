from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        ''' this is the wrapper functtion'''
        print("inside wrapper function")
        return any_func(*args,**kwargs)
    return wrapper_func

@decorator_func
def func1(a):
    '''this is func1 which takes argument '''
    print(f"this is a function with argument{a}")

@decorator_func
def sum(a,b):
    '''this is the sum of two number '''
    return a+b
@decorator_func
def mul(a,b):
    '''this is multiply of two numbers  '''
    return a*b
@decorator_func
def pow(am,b):
    ''' this is a power function'''
    print(f"the power of this is {am**b}")


pow(3,4)
print(pow.__doc__)
func1(7)
print(func1.__doc__)

c=sum(6,7)
print(c)
co=sum(int(input()),int(input()))
print(co)

print(sum.__doc__)
ti=mul(int(input()),int(input()))
print(ti)
print(mul.__doc__)
print(func1.__name__)
print(mul.__name__)
print(sum.__name__)
print(pow.__name__)