import sys
sys.stdin = open('input.txt')

w = sys.stdin.readline()
n = int(sys.stdin.readline())
for nc in range(n):
    a, i, j = list(sys.stdin.readline().split())
    temp = w[int(i):int(j)+1]
    print(temp.count(a))