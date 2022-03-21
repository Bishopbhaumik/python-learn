class Team:
    def __init__(self,name,run):
        self.name=name
        self.run=run
    def fun1(self):
        print(f"{self.name} makes {self.run}")

c=Team("Dhoni",34)
c.fun1()