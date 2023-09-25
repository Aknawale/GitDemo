from Src.inheritence import calculator


class Child(calculator):
    n=100
    def __init__(self):
        calculator.__init__(self,5,7)

    def Summatiion(self):
        return self.numm+self.n+self.summation()


obbj=Child()
print(obbj.Summatiion())