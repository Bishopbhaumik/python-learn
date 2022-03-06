from functools import wraps
import time

def calc_time(function):
    @wraps(function) 
    def wrapper(*args,**kwargs):
        t1=time.time()
        ret= function(*args,**kwargs)
        t2=time.time()
        print(t2-t1)
        return ret
    return wrapper

    

@calc_time
def my_sum(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    print(f"wrong input")


print(my_sum(1,2,3,4,5,6,7,8,21,3,4,566,78,9,89))
