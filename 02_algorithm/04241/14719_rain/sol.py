# 1. 인덱스 활용을 위해 enumerate
# 2. 배열 안에서 max 탐색
# 3. max 좌 우로 다음 sec_max 탐색
# 4. 빗물 += sec_max - arr[i]
#    범위 sec_max_idx ~ max_idx
# 5. 왼쪽은 계속 왼쪽으로만, 오른쪽은 계속 오른쪽으로만 탐색

import sys
sys.stdin = open('input.txt')

def left(start, num):    # 좌측 탐색
    global sell
    arr = block[start:num]
    temp = max(arr, key=lambda x: x[1])
    for i in range(temp[0], num):
        sell += temp[1] - arr[i][1]
    if temp[0] > 0:
        left(start, temp[0])
    else:
        return

def right(num, end):    # 우측 탐색
    global sell
    arr = block[num:end]
    temp = max(arr, key=lambda x: x[1])
    for i in range(temp[0]-num):
        sell += temp[1] - arr[i][1]
    if temp[0] < w-1:
        right(temp[0]+1, end)
    else:
        return

h, w = map(int, sys.stdin.readline().split())
block = list(enumerate(map(int, sys.stdin.readline().split())))
sell = 0    # 빗물 고인 영역

maxi = max(block, key=lambda x:x[1])

if maxi[0] > 0:    # 탐색할 구간 존재 시 함수 실행
    left(0, maxi[0])
if maxi[0] < w-1:
    right(maxi[0]+1, w)

print(sell)

# print(block)
# print(max(block, key=lambda x:x[1]))
# print(max(block, key=lambda x:x[1])[1])