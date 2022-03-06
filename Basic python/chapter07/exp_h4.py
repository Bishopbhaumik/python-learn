#custom exception


class Nametooshorterror(ValueError):
    pass
def validate(name):
    if len(name)<8:
        # raise ValueError("name is too sort")
        raise Nametooshorterror("name is too sort")
    

use=input("enter your name:")
validate(use)
print(f"hello {use}")