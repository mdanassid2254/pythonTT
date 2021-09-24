class Customer:
    def setcustomerid(self,customerid):
        self.__customerid=customerid
    def getcustomerid(self):
        return self.__customerid
    def setcustomername(self,customername):
        self.__customername=customername
    def getcustomername(self):
        return self.__customername
class regularcustomer(Customer):
    def setdiscount(self,discount):
        self.__discount=discount
    def getdiscount(self):
        return self.__discount
class pc(Customer):
    def setmemcardtype(self,memcardtype):
        self.__memcardtype=memcardtype
    def getmemcardtype(self):
        return self.__memcardtype
choice=1
list=[]
while(choice==1):
    ch=input("Enter your choise:")
    if(ch==1):
        list.append(regularcustomer())
    else:
        list.append(pc())
list1=[]
for i in range (3):
    list1.append(Customer())
    list1[i].setcustomerid(int(input(("enter id"))))
for i in list1:
    print(getopt)


