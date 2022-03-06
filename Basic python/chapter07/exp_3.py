class Mobile:
    def __init__(self,name):
        self.name=name

class Mobilestore:
    def __init__(self):
        self.mobiles=[]
    def add_mobi(self,new_mobi):
        if isinstance(new_mobi,Mobile):
          self.mobiles.append(new_mobi)
        else:
            raise TypeError("not of mobile class")

one=Mobile('Oneplus 6')
smg='samsung galaxy s8'

mobostor=Mobilestore()
print(mobostor.mobiles)
mobostor.add_mobi(one)
ti=mobostor.mobiles
print(ti[0].name)
print(mobostor.mobiles[0].name)