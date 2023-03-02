import sys
sys.stdin = open('input.txt')

def cnt(n):
    global result
    flag = True
    if 1 in arr[n]:    # i 검사 (자식 유무)
        flag = False

    b = [a[n] for a in arr]    # j 검사 (부모 유무)
    if 1 not in b:
        flag = False

    if flag:
        result += 1
    return

t = int(input())
tree = list(map(int, input().split()))

# i 열 부모, j 열 자식 번호로 저장
arr = [[0] * t for _ in range(t)]
root = 51
node = int(input())

for q in range(t):
    if tree[q] == -1:
        root = q
    else:
        arr[tree[q]][q] = 1

temp = 0
for i in range(t):
    for j in range(t):
        temp += arr[i][j]

if temp <= 1:
    if root == node:
        print(0)
    else:
        print(1)
else:
    # 연결된 자식을 삭제하는 과정
    stack = [node]
    while stack:
        n = stack.pop()
        for q in range(t):
            if arr[n][q] == 1:
                stack.append(q)
                arr[n][q] = 0

    # 본인을 삭제하는 과정
    for i in range(t):
        if arr[i][node] == 1:
            arr[i][node] = 0

    # 부모 있고 자식 없는 노드 세는 과정
    # i 열에는 1이 없고, j 열에는 있어야 함
    result = 0
    for i in range(t):
        cnt(i)

    print(result)

# 반례
# 2
# -1 0
# 1

