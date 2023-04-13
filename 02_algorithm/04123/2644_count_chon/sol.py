import sys
sys.stdin =open('input.txt')

# 타겟 숫자 개별 조상 찾기
def listup(num, l):
    queue = []
    queue.append(num)
    while queue:
        k = queue.pop(0)
        for q in range(1, m + 1):
            if family[q][k] == 1:
                l.append(q)
                queue.append(q)
    return

# 최종 반환 함수
def final(r1, r2):
    for i in range(len(r1)):
        for j in range(len(r2)):
            if r1[i] == r2[j]:
                return print(i + j)
    return print(-1)

m = int(sys.stdin.readline().strip())
family = [[0] * (m + 1) for _ in range(m + 1)]
t1, t2 = list(map(int, sys.stdin.readline().split()))
# 조상 리스트 첫 요소로 본인 추가
r1, r2 = [t1], [t2]
n = int(sys.stdin.readline().strip())

# 부모-자식 관계 2차원 배열
for _ in range(n):
    p, c = list(map(int, sys.stdin.readline().split()))
    family[p][c] = 1

listup(t1, r1)
listup(t2, r2)
final(r1, r2)