class emp:
    count=0
    def __init__(self):
        emp.count=emp.count+1
    def disp(self):
        print(emp.count)
e1=emp()
e2=emp()
e3=emp()
e1.disp()