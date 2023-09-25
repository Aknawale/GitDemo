class calculator:
    numm=1
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("This part is initialised under constructor")

    def summation(self):
        return self.a+self.b+calculator.numm


obj=calculator(3,4)
print("Addition is:-",obj.summation())
