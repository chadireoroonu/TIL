import sys
sys.stdin = open('input.txt')

def solution(arr, n):
    mini = 100
    min_idx = []
    min_num = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= mini:
                mini = arr[i][j]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == mini:
                min_idx.append(i)
                min_idx.append(j)
                min_num.append(arr[i][j])
    print(min_idx)

    mini_2 = 100
    min_idx_2 = []
    for k in range(len(min_idx)//2):
        for i in range(n):
            for j in range(n):
                if i != min_idx[i * 2]:
                    if j != min_idx[i * 2 + 1]:
                        if arr[i][j] <= mini_2:
                            mini_2 = arr[i][j]



T = int(input())
for tc in range(1, T+1):
    n = int(input())

    maxcandidates = 12
    nmax = 12

    arr = [list(map(int, input().split())) for q in range(n)]

    solution(arr, n)