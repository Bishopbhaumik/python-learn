#how to use a function into function,pass function in funtion



def abc():
    def pid():
     """it is a docstring of python inner function of function abc  """
     print("It is a inner function")
    return pid


# c=abc()
# print(c)
var=abc()
var()
print(var.__doc__)
print(var.__name__)

def mym(func,l):
    return [func(item) for item in l]

def pow(a):
    def non(b):
        return b**a
    return non

ci=pow(3)(4)
print(ci)
l=[1,2,4,5]
print(mym(lambda a:a**2,l))