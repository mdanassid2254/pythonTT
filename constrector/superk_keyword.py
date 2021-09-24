class c1:
    def __init__(self,a,b):
        print(self)
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)
        print(self)
class c2(c1):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self)
    def vol(self):
        print(self.a*self.b*self.c)
        super(c2,self).__init__(self.a,self.b)
o=c2(3,3,3)
o.vol()
o.area()