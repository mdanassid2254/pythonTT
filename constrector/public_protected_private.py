class calculater:
    def __init__(self, a, b,c):
        self.a = a
        self._b = b
        self.__c = c
    def add(self,a,b):
        self.a=a
        self._b=b
       # print(self.a+self.b)
    def sub(self,a,b):
        self.a=a
        self.__b=b
       # print(self.a-self.b)
class cal2(calculater):
    def mul(self,a,b):
        self.a=a
        self.b=b
      #  print(self.a*self.b)
    def div(self,a,b):
        self.a=a
        self.b=b
     #   print(self.a/self.b)
c=calculater(3,4,5)
print(c.a)
print(c._b)
#print(c.__c)
print(c._calculater__c)