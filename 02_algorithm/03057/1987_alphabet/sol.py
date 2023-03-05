import sys
sys.stdin = open('input.txt')

r, c = list(map(int, sys.stdin.readline().split()))
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

maxi = 0
stack = set([(0, 0, arr[0][0])])    # 순회하기 위해 안에 리스트
while stack:
    i, j, result = stack.pop()
    if len(result) > maxi:    # 따로 저장하지 않고 바로 비교
        maxi = len(result)
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] not in result:
            stack.add((ni, nj, result+arr[ni][nj]))

print(maxi)