two_seven = [] # 빈 리스트 생성
num = range(1000) # 검사할 범위를 정의

for i in num: #정의한 범위 안의 숫자에 대해
    if i % 2 == 0: # 2로 나누어 떨어질 경우 리스트에 추가
        two_seven.append(i)
    elif i % 7 == 0: # 7로 나누어 떨어질 경우 리스트에 추가
        two_seven.append(i)
    else: # 2,7로 나누어 떨어지지 않을 경우 패스
        pass

# print(twe_seven)
# 중복으로 숫자가 리스트에 담기지 않아 그대로 sum 진행
print(sum(two_seven)) # 284787