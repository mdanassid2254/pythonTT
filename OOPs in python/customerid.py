class customer:
    def setname(self):
        self.id=id
        self.name=input("enter name of customer:-")
c1 = customer()
c1.setname()
c2=customer()
c2.setname()
c3=customer()
c3.setname()
list1=[c1,c2,c3]
for i in range(len(list1)):
    list1[i].id=i
print()
for i in list1:
    print("name is:- ",i.name)
    print("customer id is:-",i.id)