import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

array.sort()

for i in array:
    print(*i)