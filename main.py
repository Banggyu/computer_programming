import random

def lotto():
    results=[]
    while len(results) < 6:
        ran_num = random.randint(1, 45)
        if ran_num in results:
            print("결과가 이미 결과 목록에 있어 추가하지 않습니다")
        else:
            results.append(ran_num)
    return results

print(lotto())
