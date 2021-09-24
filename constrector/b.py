class c1:
    def __init__(self,a,b,c):
        self.a=a   # no underscore -->public
        self._b=b  # _ --->protected
        self.__c=c # __ ---> private -> it will access in a special syntex use
class ch(c1):
    pass
c=ch(1,2,3)
print(c.a)
print(c._b)
print(c._c1__c)
#print(c.__c)
