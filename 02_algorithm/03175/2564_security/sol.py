import sys
sys.stdin = open('input.txt')

m, n = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline().strip())
total = 0
store = []
for tc in range(t):
    temp = list(map(int, sys.stdin.readline().split()))
    store.append(temp)

dh, dnum = list(map(int, sys.stdin.readline().split()))

for i in range(t):
    if dh == 1 or dh == 2:
        if store[i][0] == dh:
            total += abs(dnum - store[i][1])
        else:
            if store[i][0] == 1 or store[i][0] == 2:
                if dnum + store[i][1] + n <= (m-dnum) + (m-store[i][1]) + n:
                    total += dnum + store[i][1] + n
                else:
                    total += (m-dnum) + (m-store[i][1]) + n
            else:
                if dh == 1:
                    if store[i][0] == 3:
                        total += dnum + store[i][1]
                    else:
                        total += (m-dnum) + store[i][1]
                else:
                    if store[i][0] == 3:
                        total += dnum + (n-store[i][1])
                    else:
                        total += (m-dnum) + (n-store[i][1])
    else:
        if store[i][0] == dh:
            total += abs(dnum - store[i][1])
        else:
            if store[i][0] == 3 or store[i][1] == 4:
                if dnum + store[i][1] + m <= (n-dnum) + (n-store[i][1]) + m:
                    total += dnum + store[i][1] + m
                else:
                    total += (n-dnum) + (n-store[i][1]) + m
            else:
                if dh == 3:
                    if store[i][0] == 1:
                        total += dnum + store[i][1]
                    else:
                        total += (n-dnum) + store[i][1]
                else:
                    if store[i][0] == 1:
                        total += dnum + (m-store[i][1])
                    else:
                        total += (n-dnum) + (m-store[i][1])

print(total)