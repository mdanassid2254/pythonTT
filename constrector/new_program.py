class student:
    _name= None
    _roll=None
    _branch=None
    def __init__(self,name ,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def _displayRollAndBranch(self):
        print("roll:",self._roll)
        print("branch:",self._branch)
class RAJAT(student):
    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("name:",self._name)
        self._displayRollAndBranch()
obj=RAJAT("anas",1903480100064,"computer")
obj.displayDetails()