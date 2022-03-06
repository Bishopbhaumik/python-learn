from csv import reader,DictWriter

with open("cs_1.csv",'r') as f:
    n=reader(f)
    print(n)
    # print("\t".join(str([i for i in n])))
    for i in n:
        print(i)
# dic={
#      'name':input(),
#       'age':int(input())


# }
# print(dic)