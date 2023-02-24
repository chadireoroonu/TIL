import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

maxi = 0
mini = 0
# 현재 위치를 포함하므로 temp 초기값은 1
temp = 1
# 숫자가 같거나 커질 경우 temp +1
# 아니면 maxi 비교 후 재할당 혹은 버림
for w in range(n-1):
    if num[w] >= num[w+1]:
        temp += 1
    else:
        if temp > maxi:
            maxi = temp
        temp = 1

# 반복문이 끝난 후 남아있는 temp 처리
if temp:
    if temp > maxi:
        maxi = temp
temp = 1

# 숫자가 같거나 작아지는 경우 temp +1
# 아니면 mini 비교 후 재할당 혹은 버림
for w in range(n-1):
    if num[w] <= num[w+1]:
        temp += 1
    else:
        if temp > mini:
            mini = temp
        temp = 1

# 반복문이 끝난 후 남아있는 temp 처리
if temp:
    if temp > mini:
        mini = temp

# maxi, mini 중 큰 값 출력
if maxi > mini:
    print(maxi)
else:
    print(mini)