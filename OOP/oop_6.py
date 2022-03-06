#multiple inheritence
class A:
    def cas_a_m(self):
        print("it is just a class a method")
    def hello(self):
        print("hello from class a")

class B:
    def cas_b_m(self):
        print("it is just a class b method")
    def hello(self):
        print("hello from class b")

class C(A,B):
    pass


ci=C()
ci.cas_a_m()
ci.cas_b_m()
ci.hello()