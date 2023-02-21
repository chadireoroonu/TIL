import sys
sys.stdin = open('input.txt')

# 한 줄 col에서 한개씩 골라서 전체 합 cnt 구하기
def search(col, cnt):
    global result
    if cnt > result:
        return
    if col == N:
        if cnt < result:
            result = cnt
    else:
        for row in range(N):
            if not visited[row]:
                visited[row] = 1
                search(col+1, cnt+arr[col][row])
                visited[row] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = N * 10 * N
    visited = [0] * N
    search(0, 0)
    print(f'#{tc} {result}')
