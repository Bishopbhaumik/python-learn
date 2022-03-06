from functools import wraps
def printfunction_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"you are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper
@printfunction_data
def sum(a,b):
    '''this is the sum of two number '''
    return a+b
    


print(sum(4,5))