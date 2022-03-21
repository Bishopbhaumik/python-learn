#example of single inheritence.

class Indgames():
    def first(self):
        print("There are many indoor games")

class chess(Indgames):
    def second(self):
        print("chess is one of them")
        
obj=chess()
obj.first()
obj.second()