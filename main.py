first = {"고객명":"김지구", "잔액":1350, "마지막 거래일":2023-10-21}
second = {"고객명":"이화성", "잔액":3000000, "마지막 거래일":2021-8-21}
third = {"고객명":"신목성", "잔액":100300, "마지막 거래일":2024-3-28}

db = {"김지구":{first["잔액"]}, "이화성":{second["잔액"]}, "신목성":{third["잔액"]}}
print(db["이화성"])
