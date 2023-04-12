# t1, t2 조상 리스트 추가
# 공통 조상의 각 인덱스 합 출력

# 부모-자식이면, 공통 조상을 찾기 전 정답 출력

import sys
sys.stdin = open('input.txt')

def find(n1, n2):
    if parent[n1] == n2 or parent[n2] == n1:
        print(1)
        return
    listup(t1, r1)
    listup(t2, r2)
    print(f'r1 {r1}')
    print(f'r2 {r2}')
    final()
    return

def listup(num, l):
    queue = []
    queue.append(num)
    while queue:
        k = queue.pop(0)
        if parent[k]:
            l.append(parent[k])
            queue.append(parent[k])
    return

def final():
    result = -1
    for i in range(len(r1)):
        for j in range(len(r2)):
            if r1[i] and r1[i] == r2[j]:
                result = i + j + 2

    print(result)
    return

m = int(sys.stdin.readline().strip())
t1, t2 = list(map(int, sys.stdin.readline().split()))
r1, r2 = [], []
n = int(sys.stdin.readline().strip())

parent = [0] * (m+1)
left = [0] * (m+1)
right = [0] * (m+1)
for _ in range(n):
    p, c = list(map(int, sys.stdin.readline().split()))
    if left[p]:
        right[p] = c
    else:
        left[p] = c
    parent[c] = p
print(t1, t2)
print(parent)
print(left)
print(right)

find(t1, t2)