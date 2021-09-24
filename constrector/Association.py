class computer:
    def writecode(self,text):
        print("written in editor")
    def execute(self):
        print("code executed")
class student:
    def dolabassigment(self,computer,assignment):
        computer.writecode(assignment)
        computer.execute()
c=computer()
s=student()
s.dolabassigment(c,"Assignment code")
#Association, example-student solves lab assignment using computer.