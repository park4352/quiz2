환율 = {"달러": 1320, "엔": 950, "위안": 182 }
wm = input("금액 종류를 입력하시오: ")
num, currency = wm.split()

print("철수가 가지고 있는 돈의 원화 가치는", float(num) * 환율[currency], "원입니다")



