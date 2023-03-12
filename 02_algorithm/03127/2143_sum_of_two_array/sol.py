import sys
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr_a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_b = list(map(int, sys.stdin.readline().split()))

num_a = [0] * (n+1)
num_b = [0] * (m+1)

def full(arr1, arr2, p):
    for w in range(p):
        arr1[w+1] = arr2[w] + arr1[w]
    return

full(num_a, arr_a, n)
full(num_b, arr_b, m)

count = 0
front_a = 0
front_b = 0
rear_a = 0
rear_b = 0
while rear_a < n and rear_b < m:
    if num_a[rear_a] - num_a[front_a] + num_b[rear_b] - num_b[front_b] == t:
        count += 1
    if