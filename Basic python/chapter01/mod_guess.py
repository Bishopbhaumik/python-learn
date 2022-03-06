import random

wi=random.randint(0,9)

a=int(input("Guess the no:--"))
c=1
p=a

while p!=wi:
    if wi==a:
     print("YOU WIN THE GAME\n CONGRATS!!!")
     print(f"The actual no is {wi}")
     break
    elif wi<a:
     print("you entered a higher no than actual number>")
    
    elif wi>a:
     print("You enterd a lower no than the actual no")
    c+=1
    a=int(input("Guess the no:--"))
print(f"you win the game in your {c}th try")
