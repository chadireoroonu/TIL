num1 = int(input())
num2 = int(input())

print(num1+num2)


lunch = {'떡볶이': 8000, '평양냉면': 12000, '돈까스': 11000, '양념갈비': 15000}

money = dict.values(lunch) # 값들로 구성된 새로운 리스트 생성

print(sum(money)/len(money)) # 점심값들의 합 / 점심값 개수 # 11500.0