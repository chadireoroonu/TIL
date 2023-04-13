import sys
sys.stdin = open('input.txt')

# 초대하는 사람 판별 함수
def invite(num):
    people = 0
    visited = [0] * (n+1)
    visited[num] = 1
    queue = [num]
    while queue:
        i = queue.pop(0)
        for j in range(1, n+1):
            if friend[i][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = visited[i] + 1

    # 친구의 친구까지 -> visited 숫자가 3이하
    for k in range(2, n+1):
        if visited[k] and visited[k] <= 3:
            people += 1

    return print(people)


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

friend = [[0] * (n+1) for _ in range(n+1)]

# 2차원 배열에 친구 관계 저장
for _ in range(m):
    p, f = list(map(int, sys.stdin.readline().split()))
    friend[p][f] = friend[f][p] = 1

invite(1)