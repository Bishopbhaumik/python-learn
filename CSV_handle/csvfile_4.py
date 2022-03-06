from csv import DictWriter
with open("cs_2.csv",'w',newline='') as f:
    cvr=DictWriter(f,fieldnames=['Firstname','lastname','country'])
    cvr.writeheader()
    n=int(input("enter rows:"))
    for i in range(0,n):
        cvr.writerow({'Firstname':input("enter first name:"),
                     'lastname':input("enter last name:"),
                      'country':input("enter country:")
        
        
                    }
        
        
        
        )
# input("enter country:")
# input("enter first name:")
# input("enter last name:")