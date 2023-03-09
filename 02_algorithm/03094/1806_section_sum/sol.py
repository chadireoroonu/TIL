import sys
sys.stdin = open('input.txt')

n, s = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for i in range(n):
    num[i+1] = number[i] + num[i]

def sol(arr, n, m):
    for k in range(n, m, -1):
        if arr[k] - arr[k-m] >= s:
            return print(j)
    else:
        return sol(arr, n-1)

flag = True
for i in range(n):
    if num[i] >= s:
        flag = False

if flag == True:
    sol(num, n, n)

else:
    print(1)