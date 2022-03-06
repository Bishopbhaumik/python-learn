#exception handeling
#try except else finally
while True:
    try:
        age=int(input("enter age:"))
        break
    except ValueError:#only except also work
        print("invalid input")
    except:
        print("unexpeted input")

if age<18:
        print("ypu can not play")
else:
        print("you can play")



