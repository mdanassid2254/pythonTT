class A:
    def f1(self):
        print("A")
class B:
    def f2(self):
        print("B")
class C:
    def f3(self):
        print("C")
class ch(A,B,C):
    pass
och=ch()
och.f1()
och.f2()
och.f3()