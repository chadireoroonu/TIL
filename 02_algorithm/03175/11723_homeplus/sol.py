import sys
sys.stdin = open('input.txt')

# 시간초과 오답
M = int(sys.stdin.readline().strip())
S = set()    # 겹치는 원소 없도록 set 설정
for _ in range(M):
    i = list(sys.stdin.readline().split())
    if i[0] == 'add':
        S.add(i[1])
    elif i[0] == 'remove':
        if i[1] in S:
            S.remove(i[1])
    elif i[0] == 'check':
        if i[1] in S:
            print(1)
        else:
            print(0)
    elif i[0] == 'toggle':
        if i[1] in S:
            S.remove(i[1])
        else:
            S.add(i[1])
    elif i[0] == 'all':
        for j in range(1, 21):
            if str(j) not in S:
                S.add(str(j))
    elif i[0] == 'empty':
        S = set()