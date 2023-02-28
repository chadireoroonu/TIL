import sys
sys.stdin = open('input.txt')

def find(l, r, f):
    count = 1
    start = l
    end = r
    while start <= end:
        if (start+end)//2 == f:
            return count
        else:
            if (start+end)//2 < f:
                start = (start+end)//2
            elif (start+end)//2 > f:
                end = (start+end)//2
        count += 1

T = int(input())
for tc in range(1, T+1):
    r, a, b = list(map(int, input().split()))

    if find(1, r, a) < find(1, r, b):
        print(f'#{tc} A')
    elif find(1, r, a) > find(1, r, b):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')