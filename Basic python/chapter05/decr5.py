from functools import wraps

def only_da(data):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data for arg in args]):
               return func(*args,**kwargs)
            else:
              print("invalid") 
        return wrapper
    return decorator

@only_da(str)
def si(*args):
    strings=''
    for i in args:
        strings+=i
    return strings

print(si("Bishop","Bhaumik"))
print(si("Bishop","Bhaumik",12))