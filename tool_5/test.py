class a:
    def test1(self):
        print("a called")
class b(a):
    def test(self):
        print("b called")
class c(a):
    def test(self):
        print("c called ")
class d(b,c):
    def test2(self):
        print("xcv")
        
obj=d()
obj.test()