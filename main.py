dot = int(input("몇 단까지 출력할까요?"))

for i in range(1,dot+1):
    print("-----[",i,"단]-----")
    for j in range(1, i+20-i):
        print(i,"*",j,"=",i * j)

