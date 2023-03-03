import sys
sys.stdin = open('input.txt')

n, k = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))

maxi = 0
for i in range(n-k+1):
    temp = 0
    for j in range(k):
        temp += num[i+j]
    if temp > maxi:
        maxi = temp

print(maxi)