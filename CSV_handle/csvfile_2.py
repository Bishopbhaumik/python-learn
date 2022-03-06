from csv import writer
with open("cs_2.csv",'w',newline='') as f:
    cvr=writer(f)
    # cvr.writerow(['name','country'])
    # cvr.writerow(['Bishop','India'])
    # cvr.writerow(['Harshit','India'])
    # cvr.writerow(['Mahejabin','Bangladesh'])
    cvr.writerows([['name','country'],['Bishop','India'],['Harshit','India'],['Mahejabin','Bangladesh']])