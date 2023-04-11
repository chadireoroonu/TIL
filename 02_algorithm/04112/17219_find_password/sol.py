import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
site = {}
for i in range(n):
    a, b = list(sys.stdin.readline().split())
    site[a] = b

for i in range(m):
    temp = sys.stdin.readline().strip()
    print(site[temp])