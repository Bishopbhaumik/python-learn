from functools import wraps
def only_int(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # data=[]
        # for arg in args:
        #     data.append(type(arg)==int)
        # if all(data):
        #     return func(*args,**kwargs)
        # else:
        #     print("invalid")
        if all([type(arg)==int for arg in args]):
            return func(*args,**kwargs)
        print("invalid")
    return wrapper
        
@only_int
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total


print(add_all(1,2,3,4,5,6,7,8,9,9,12))
print(add_all(1,2,3,4,5,8.9,7.8,'Bishop'))