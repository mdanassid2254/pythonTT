class calc:
    def sum1(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)

    def mul(self, a, b):
            self.a = a
            self.b = b
            print(self.a * self.b)
    def divide(self, a, b):
            self.a = a
            self.b = b
            print(self.a/self.b)
    def sub(self, a, b):
                self.a = a
                self.b = b
                print(self.a-self.b)
calc1 = calc()
calc1.sum1(4,4)
calc2=calc()
calc2.mul(5,6)
calc3 = calc()
calc3.divide(16, 8)
calc4=calc()
calc4.sub(6, 4)
