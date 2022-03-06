def sublist_count(l):
    count=0
    for i in l:
        if type(i)== list:
            count+=1

    return count

toli=[1,2,2,3,[4,5,6],7,8,4,[7,3,4,5,],[3,7,0],[8,3],34,56]

print(sublist_count(toli))