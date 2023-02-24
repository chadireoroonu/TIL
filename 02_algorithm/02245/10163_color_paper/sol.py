import sys
sys.stdin = open('input.txt')

# 문제에서 주어진 크기의 배열 생성
# 첫 숫자 동안 반복
# 색종이의 왼쪽 위 좌표와 너비, 높이를 저장
arr = [[0] * 1001 for _ in range(1001)]
n = int(sys.stdin.readline())
for nc in range(n):
    i, j, x, y = list(map(int, sys.stdin.readline().split()))

    # 색종이의 크기 만큼 배열에서 +1 저장
    # 만약 다음 색종이가 주어진다면, 숫자가 달라질 것
    for a in range(i, i+x):
        for b in range(j, j+y):
            arr[a][b] += 1

# 1~n+1 범위동안 전 배열을 순회하며
# 저장된 값이 현재 반복 수 값인 칸 수를 출력
for result in range(1, n+1):
    total = 0
    for a in range(1001):
        for b in range(1001):
            if arr[a][b] == result:
                total += 1
    print(total)

