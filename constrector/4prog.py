class super:
    var1 = None
    _var2 = None
    __var3 = None
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3
    def displayPublicMembers(self):
        print("Public data member:",self.var1)

    def _displayProtectedMembers(self):
            print("Public data member:",self._var2)
    def __displayPrivateMembers(self):
        print("Public data member:",self.__var3)
    def accessPrivateMembers(self):
        self.__displayPrivateMembers()
class sub(super):
    def __init__(self,var1,var2,var3):
        super.__init__(self,var1,var2,var3)
    def accessProtectMembers(self):
        self._displayProtectedMembers()
obj =sub("anas",64,"psit")
obj.displayPublicMembers()
obj.accessProtectMembers()
obj.accessPrivateMembers()
print("objectvis accessed =",obj._var2)