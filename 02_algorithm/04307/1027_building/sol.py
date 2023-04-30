# 1. 모든 건물에 대해 좌, 우 방향 탐색
# 2. 볼 수 있는 건물의 개수 세기
#    발견한 옆 건물 높이 기록 buildings[i] > 건물 => h = 0
#    1. 좌측탐색
#       1. h == 0 and buildings[j] < buildings[i]
#          기울기 : (buildings[i]-buildings[j]) / (i-j) 기록
#          기록된 숫자보다 기울기가 작으면 temp += 1, 기울기 재할당
#       2. h == 0 and buildings[j] > buildings[i]
#          temp += 1, h = 1
#          기울기 : (buildings[i]-buildings[j]) / (i-j) 기록
#       3. h == 1 and buildings[j] > buildings[i]
#          기록된 숫자보다 기울기가 작으면 temp += 1, 기울기 재할당
#       4. h == 1 and buildings[j] < buildings[i]
#          그냥 넘어가기
# 3. maxi 보다 크다면 재할당
# 4. 최종 maxi 값 출력

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
buildings = list(map(int, sys.stdin.readline().split()))
maxi = 0

for i in range(N):
    temp = 0
    h, r = 0, 1000000001
    for j in range(i-1, -1, -1):
        if h:
            if (buildings[i] - buildings[j]) / (i - j) < r:
                r = (buildings[i] - buildings[j]) / (i - j)
                temp += 1
                print(f'i={i}, j={j}, r={r}')
        else:
            if buildings[j] < buildings[i] and (buildings[i] - buildings[j]) / (i - j) < r:
                r = (buildings[i] - buildings[j]) / (i - j)
                temp += 1
                print(f'i={i}, j={j}, r={r}')
            elif buildings[j] > buildings[i]:
                r = (buildings[i] - buildings[j]) / (i - j)
                temp += 1
                h = 1
                print(f'i={i}, j={j}, r={r}')
            elif buildings[j] == buildings[i]:
                r = 0
                temp += 1
                h = 1
                print(f'i={i}, j={j}, r={r}')
    h = r = 0
    for j in range(i + 1, N):
        if h:
            if (buildings[j] - buildings[i]) / (j - i) > r:
                r = (buildings[j] - buildings[i]) / (j - i)
                temp += 1
                print(f'i={i}, j={j}, r={r}')
        else:
            if buildings[j] < buildings[i] and (buildings[i] - buildings[j]) / (j - i) > r:
                r = (buildings[j] - buildings[i]) / (j - i)
                temp += 1
                print(f'i={i}, j={j}, r={r}')
            elif buildings[j] > buildings[i]:
                r = (buildings[j] - buildings[i]) / (j - i)
                temp += 1
                h = 1
                print(f'i={i}, j={j}, r={r}')
            elif buildings[j] == buildings[i]:
                r = 0
                temp += 1
                h = 1
                print(f'i={i}, j={j}, r={r}')

    print(f'i={i}, temp={temp}')
    if temp > maxi:
        maxi = temp

print(maxi)