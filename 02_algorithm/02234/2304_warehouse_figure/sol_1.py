import sys
sys.stdin = open('input.txt')

def left(arr):
    global total
    Flag = True
    while Flag:
        left_maxi = max(arr)
        left_idx = arr.in


        return left(arr[:idx])

arr = [0] * 1000
n = int(sys.stdin.readline())
idx = 0
maxi = 0
total = 0
for i in range(n):
    w, h = list(map(int, input().split()))
    arr[w] = h
    if h > maxi:
        maxi = h
        idx = w
total = maxi





