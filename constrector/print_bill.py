class pd:
    __counter=100
    def calculatebill(self,item,quantity):
        self.d={"tv":20000,"ac":50000}
        for k in self.d.keys():
            if k==item:
                self.__billamount=self.d[k]*quantity
    def dispbill(self):
        o=pd()
        o.scanchar("*")
        o.ph(20)
        o.ph1("Easy Shop")
        o.ph(20)
    def getbillamount(self):
        return self.__billamount
    def purchasebill(self,billamount):
        self.__billamount=billamount
        pd.__counter+=1
        self.billid=pd.__counter
        print(self.getbillid())
        print(self.__billamount)
        self.dispbill()
class printbill:
    def printbills(self):
        print("*"*20)

