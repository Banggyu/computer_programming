<<<<<<< HEAD
menu = ["냉면", "볶음밥", "피자", "짜장면"]

try:
    choose = int(input("원하는 메뉴의 숫자를 입력하세요: "))
    if choose < 1 or choose > 4:
        raise IndexError

    selected_menu = menu[choose - 1]
    print((selected_menu) + "음식을 선택하셨습니다.")


except ValueError:
    print("숫자를 입력하십시오. ")

except IndexError:
    print("1~4 사이의 숫자를 입력하십시오.")
=======
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
>>>>>>> 24011d1eaa535e2bdf88bffe9dbd54069772dcde
