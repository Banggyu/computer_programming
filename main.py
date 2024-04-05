score = input("점수를 입력하시오: ")

if int(score) >= 71:
    print("A")

if int(score) >= 41 and int(score) <= 70:
    print("B")

if int(score) >= 11 and int(score) <= 40:
    print("C")

if int(score) <= 10:
    print("D")
