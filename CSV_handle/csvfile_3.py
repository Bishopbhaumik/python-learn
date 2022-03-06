from csv import DictWriter
with open("cs_2.csv",'w',newline='') as f:
    cvr=DictWriter(f,fieldnames=['Firstname','lastname','country'])
    cvr.writeheader()
    cvr.writerows([
        {'Firstname':'Mohini','lastname':'sen','country':'India'},
        {'Firstname':'Harshit','lastname':'Vashisth','country':'India'},
        {'Firstname':'sonya','lastname':'hussain','country':'Bangladesh'},
        {'Firstname':'trisha','lastname':'karandikar','country':'Bangladesh'}
    ])
    # cvr.writerow({'Firstname':'Mohini','lastname':'sen','country':'India'})
    # cvr.writerow({'Firstname':'Harshit','lastname':'Vashisth','country':'India'})
    # cvr.writerow({'Firstname':'sonya','lastname':'hussain','country':'Bangladesh'})
    # cvr.writerow({'Firstname':'trisha','lastname':'karandikar','country':'Bangladesh'})