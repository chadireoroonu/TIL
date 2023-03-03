import sys
sys.stdin = open('input.txt')

def binggo(arr, goal):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == goal:
                arr[i][j] = 26
    # if count >= 15 조건을 달았었는데, 잘못생각함
    line = 0    # 가로줄 빙고 검사
    for i in range(5):
        if sum(arr[i]) == 130:
            line += 1

    for i in range(5):    # 세로줄 빙고 검사
        j = [a[i] for a in arr]
        if sum(j) == 130:
            line += 1

    temp = 0    # 음의 기울기 대각선 빙고 검사
    for i in range(5):
        for j in range(5):
            if i == j:
                temp += arr[i][j]
    if temp == 130:
        line += 1

    temp = 0    # 양의 기울기 대각선 빙고 검사
    for i in range(5):
        for j in range(5):
            if i+j == 4:
                temp += arr[i][j]
    if temp == 130:
        line += 1

    if line >= 3:    # 완성된 줄이 3 이상이면 빙고
        result.append(count)
        return

    return

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
num = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

result = []
count = 1
for a in range(5):
    for b in range(5):
        binggo(arr, num[a][b])
        count += 1

print(result[0])