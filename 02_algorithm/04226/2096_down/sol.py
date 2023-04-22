# 최대값 배열, 최소값 배열을 저장, n줄 동안 배열 한 줄 씩 입력 받기
# 함수 -> 입력 받은 배열과 최대값, 최소값 배열 더해 최대값 갱신
# 비교를 위해 temp 배열 사용, 마지막에 maxi = temp
# 반복문 후 maxi 최대값, mini 최소값 출력

import sys
sys.stdin = open('input.txt')

def down():    # 최대값, 최소값 배열 갱신
    global maxi, mini
    maxi_temp = [0]*3
    mini_temp = [10*n]*3
    for x in range(3):
        dx = [-1, 0, 1]
        for y in range(3):
            nx = x + dx[y]
            if 0 <= nx < 3 and maxi[x] + arr[nx] > maxi_temp[nx]:
                maxi_temp[nx] = maxi[x] + arr[nx]
            if 0 <= nx < 3 and mini[x] + arr[nx] < mini_temp[nx]:
                mini_temp[nx] = mini[x] + arr[nx]
    maxi = maxi_temp
    mini = mini_temp
    return maxi


n = int(sys.stdin.readline().strip())
maxi = mini = [0] * 3    # 최대, 최소 배열 선언
for t in range(n):
    arr = list(map(int, sys.stdin.readline().split()))    # 한 줄 입력
    down()    # 최대값 찾기 함수

print(f'{max(maxi)} {min(mini)}')