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