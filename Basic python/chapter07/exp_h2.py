#try except else finally
while True:
    try:
        number=int(input("enter age:"))
        
    except ValueError:#only except also work
        print("invalid input")
    except:
        print("unexpeted input")
    else:
        print(f"user inputed {number}")
        break
    finally:
        print("It is Bishop Bhaumik................")

