class Calc():
    def __init__(self,num1,num2):
        self.num1 = int(input("Escribe el primer numero: "))
        self.num2 = int(input("Escribe el segundo numero: "))
    def sum(self):
        sum = self.num1 + self.num2
        print(sum)    
    def res(self):
        res = self.num1 - self.num2
        print(res)
    def mul(self):
        mul = self.num1 * self.num2
        print(mul)
    def div(self):
        div = self.num1 / self.num2
        print(div)

def main():

    operacion1 = Calc(0,0)
    operacion1.sum()
    operacion1.res()
    operacion1.mul()
    operacion1.div()
main()


