class calculater:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(self.a-self.b)
class cal2(calculater):
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(self.a*self.b)
    def div(self,a,b):
        self.a=a
        self.b=b
        print(self.a/self.b)
c=cal2(3,5)
print(c.mul(3,5))

