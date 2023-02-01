# num1 = int(input())
# num2 = int(input())

# print(num1+num2)

# {key: value}
# key에 들어갈 수 있는 값은 Immutable(불변형) -> string
# value에 들어갈 수 있는 값은 -> 상관없음
# lunch = {'떡볶이': 8000, '평양냉면': 12000, '돈까스': 11000, '양념갈비': 15000}

# money = dict.values(lunch) # 값들로 구성된 새로운 리스트 생성

# print(sum(money)/len(money)) # 점심값들의 합 / 점심값 개수 # 11500.0

# while은 부적절 -> 지금은 반복횟수를 알 수 없기 때문에

menu = {'김치찌개': 10000, '라면': 20000}

result = 0
count = 0
for some_value in menu:
    print(menu[some_value])
    result = result + menu[some_value]
    count += 1
print(result//count)