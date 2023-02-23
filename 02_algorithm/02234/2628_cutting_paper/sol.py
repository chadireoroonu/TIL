import sys
sys.stdin = open('input.txt')

w, h = list(map(int, sys.stdin.readline().split()))
paper = [[1] * w for _ in range(h)]

cut = []
n = int(sys.stdin.readline())
for nc in range(n):
    line = list(map(int, input().split()))
    cut.append(line)

cut = sorted(cut, reverse= True)
print(cut)
for i in cut:
    if i[0] == 1:
        if i[1] > w // 2:
            for 
