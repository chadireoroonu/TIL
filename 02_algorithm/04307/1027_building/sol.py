# 1. 모든 건물에 대해 좌, 우 방향 탐색
# 2. 볼 수 있는 건물의 개수 세기
#    1. 좌측탐색 -> 기울기 -
#       기울기 : (buildings[i] - buildings[j]) / (i - j)
#    2. 우측탐색 -> 기울기 +
#       기울기 : (buildings[j] - buildings[i]) / (j - i)
# 3. maxi 보다 크다면 재할당
# 4. 최종 maxi 값 출력

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
buildings = list(map(int, sys.stdin.readline().split()))
maxi = 0

for i in range(N):
    temp = 0
    r = 1000000001
    for j in range(i-1, -1, -1):    # 좌측탐색
        if (buildings[i] - buildings[j]) / (i - j) < r:
            r = (buildings[i] - buildings[j]) / (i - j)
            temp += 1
    r = -1000000001
    for j in range(i + 1, N):    # 우측탐색
        if (buildings[j] - buildings[i]) / (j - i) > r:
            r = (buildings[i] - buildings[j]) / (i - j)
            temp += 1

    if temp > maxi:
        maxi = temp

print(maxi)