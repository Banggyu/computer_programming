class Beverage:

    def __init__(self, name, quantity):
        self.menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}
        self.name = name
        self.quantity = quantity
        self.total = 0

    def calculate(self):
        if self.name == "커피" or self.name == "녹차" or self.name == "아이스티":
            self.total += self.menu[self.name]*int(self.quantity)
            print(self.menu)
        else:
            print("메뉴를 잘못 입력하셨습니다.")


user_input_1 = input("메뉴를 선택하세요")

user_input_2 = input("수량을 입력하세요")
order = Beverage(user_input_1, user_input_2)
order.calculate()
print(order.total)
