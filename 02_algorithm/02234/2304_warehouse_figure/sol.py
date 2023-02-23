import sys
sys.stdin = open('input.txt')

def find_left(arr):
    global total
    if len(arr) == 0:
        return
    else:
        maxi = [0, 0]
        for i in arr:
            if i[1] > maxi[1]:
                maxi = i
        print(maxi[1] * (maxi[0]-arr[0][0]))
        total += maxi[1] * (maxi[0]-arr[0][0])
        idx = arr.index(maxi)
    print(total)
    return find_left(arr[:idx])


def find_right(arr):
    global total
    if len(arr) == 0:
        return
    else:
        maxi = [0, 0]
        for i in arr:
            if i[1] > maxi[1]:
                maxi = i
        total += maxi[1] * (arr[-1][0]-maxi[0])
        idx = arr.index(maxi)
        print(total)
    return find_right(arr[idx+1:])

n = int(sys.stdin.readline())
high = []
maxi1 = [0, 0]
total = 0
for nc in range(n):
    h = list(map(int, sys.stdin.readline().split()))
    if h[1] > maxi1[1]:
        maxi1 = h
    high.append(h)

total += maxi1[1]
high = sorted(high)

print(total)

idx1 = high.index(maxi1)
find_left(high[:idx1])
# find_right(high[idx1+1:])
print(total)
print(high)