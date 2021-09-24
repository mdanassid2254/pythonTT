class rajat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayAge(self):
        print("age:",self.age)
obj=rajat("anas",20)
print("name:",obj.name)
obj.displayAge()