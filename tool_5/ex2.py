class Indgames():
    def first(self):
        print("There are many indoor games")

class chess(Indgames):
    super().first()
    def second(self):
        print("chess is one of them")
        
obj=chess()

obj.second()