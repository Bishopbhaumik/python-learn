from csv import reader,writer,DictWriter,DictReader
with open("cs_1.csv",'r') as rf:
    with open("cs_3.csv",'w',newline='') as wf:
        cvr=DictReader(rf)
        cvw=DictWriter(wf,fieldnames=['fname','rl','mobile'])
        cvw.writeheader()
        for row in cvr:
            fna,mi,ct=row['name'],row['roll'],row['phoneno']
            cvw.writerow({'fname':fna.upper(),'rl':mi,'mobile':ct})