def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print("it is zero division  error")
        print(err)

while True:
    try:
        a=int(input("first number:"))
        b=int(input("devisor:"))
    except TypeError:
        print("please enter correct type.")
    except:
        print("unexpected interrupt")
    else:
        print(devide(a,b))
        break
    finally:
        print("it is done.................")