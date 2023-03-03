import sys
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
load = []
for i in range(6):
    a, b = list(map(int, sys.stdin.readline().split()))
    load.append(b)


l = load.index(max(load))
temp = load[(l+1)%6] * load[(l+2)%6] + load[(l+4)%6] * load[(l+5)%6]

print(temp*t)