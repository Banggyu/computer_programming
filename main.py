def registration_number(identity_number):
    if len(identity_number) != 14:
        return False

    if identity_number[6] != '-':
        return False

    identity_number = identity_number.replace('-', '')

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = sum(int(identity_number[i]) * weights[i] for i in range(12))
    remainder = (11 - total % 11) % 10

    return remainder == int(identity_number[12])


id_card_number = input("주민등록번호를 입력하십시오: ")
if registration_number(id_card_number):
    print("주민등록번호가 일치합니다.")
else:
    print("주민등록번호가 일치하지 않습니다.")
