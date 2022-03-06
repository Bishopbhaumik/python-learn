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
    def __str__(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"
    def __repr__(self):
        return f"Phone(\'{self.brand}' ,\'{self.model_name}',{self.price})"
    def __len__(self):
        return len(self.full_name())
        
Phone1=Phone('Nokia','1150',8000)
print(len(Phone1))
print(Phone1)