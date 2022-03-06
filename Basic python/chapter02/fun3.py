numbers=[1,2,4,5,7]
names=['Bishop','shaibal','saamantha','pallavi','rashmika']
students={
     'Bishop':{'score':98,'age':20},
     'sourav':{'score':97,'age':21},
     'trishit':{'score':99,'age':22}
}
student2=[
    {'name':'Bishop','score':98,'age':20},
    {'name':'sourav','score':97,'age':21},
    {'name':'trishit','score':99,'age':22}
]
print(max(numbers))
print(max(names,key=lambda item:len(item)))
# print(max(names))
print(max(students,key=lambda item:students[item]['score']))
print(max(students,key=lambda item:students[item]['age']))
print(max(student2,key=lambda item:item.get('score')))
print(max(student2,key=lambda item:item.get('score'))['score'])
