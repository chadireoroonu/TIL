import sys
sys.stdin = open('input.txt')

def DFS(load, stack):
    stack = [start]

for q in range(10):
    tc, e = list(map(int, input().split()))
    data = list(map(int, input().split()))
    load = [[0] * 100 for _ in range(100)]

    for i in range(e):
        load[data[i*2]][data[i*2+1]] = 1

    print(load)
