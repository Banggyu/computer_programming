class Bun:
    def __init__(self, custard_cream, price):
        self.content = custard_cream
        self.price = 1000
        self.total = 0


    def sell(self):
        self.total += self.price
        print(self.content + "붕어빵이 판매되었습니다")

custard_cream_bun = Bun("슈크림", 1000)
custard_cream_bun.sell()
custard_cream_bun.sell()

print("누적 판매는" , custard_cream_bun.total , "입니다")

