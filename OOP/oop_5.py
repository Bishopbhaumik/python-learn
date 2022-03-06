#example of inheritence
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        # self.__price=price
        self.price=max(price,0)
        # self.complete_sp=f"{self.brand} {self.model_name} and price {self.price}"
    def make_a_call(self,phone_no):
        print(f"calling {phone_no}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,mem,rc):
        #two ways
        # Phone.__init__(self,brand,model_name,price)#uncommon way
        super().__init__(brand,model_name,price)#common way
        self.ram=ram
        self.memory=mem
        self.rear=rc
    def full_name(self):#method overriding
        return f"{self.brand} {self.model_name} {self.price}"
class Flg(Smartphone):
    def __init__(self,brand,model_name,price,ram,mem,rc,fc):
        super().__init__(brand,model_name,price,ram,mem,rc)
        self.front=fc
    def full_name(self):
        return f"{self.brand} {self.model_name} {self.price} and camera {self.rear}"
        # return super().full_name()



s=Smartphone("Oneplus",5,46000,"4gb","64 gb","13 mp")
print(s.full_name())
f=Flg("Oneplust",5,46000,"4gb","64 gb","13 mp","8mp")
print(f.full_name())
# print(help(Flg))
print(isinstance("Oneplust",Flg))
print(issubclass(Smartphone,Phone))