import random

wi=random.randint(0,9)

a=int(input("Guess the no:--"))

if wi==a:
    print("YOU WIN THE GAME\n CONGRATS!!!")
elif wi<a:
    print("you entered a higher no than actual number>")
elif wi>a:
    print("You enterd a lower no than the actual no")

print(f"The actual no is {wi}")


print("nice tutorial\n"*10)

