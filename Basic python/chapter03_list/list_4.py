fruit=['Mango','Apple','Banana','Orange','grape','peer','grape','kiwi']
print(fruit)
if 'grape' in fruit:
    print("present")
else:
    print("Not present")
print(fruit.count('grape'))
fruit.sort()
print(fruit)
nu=[3,1,8,5,10]
print(nu)
nu.sort()
print(nu)
nu_cop=nu.copy()
nu.clear()
print(nu)
print(nu_cop)