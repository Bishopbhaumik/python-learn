# Encapsulation
# abstruction
# namemangling
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        # self.__price=price        #namemangling
        self.price=max(price,0)
        # self.complete_sp=f"{self.brand} {self.model_name} and price {self.price}"
    def make_a_call(self,phone_no):
        print(f"calling {phone_no}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    @property  #to update without init
    def complete_sp(self):
        return f"{self.brand} {self.model_name} and price {self.price}"

    #getter setter
    @property
    def pri(self):
        return self.price
    @pri.setter
    def pri(self,np):
        self.price=max(np,0)


Phone1=Phone('Nokia','1150',8000)
# print(Phone1.__dict__)
# print(Phone1._Phone__price)
# print(Phone1.full_name())
# print(Phone1.brand)
# print(Phone1.model_name)
print(Phone1.price)
print(Phone1.complete_sp)
Phone1.price=-345
print(Phone1.price)
print(Phone1.complete_sp)
Phone1.pri=-678
print(Phone1.price)
print(Phone1.complete_sp)






