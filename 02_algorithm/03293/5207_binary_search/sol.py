import sys
sys.stdin = open('input.txt')

def binary(n, arr):
    global check, count
    start = 0
    end = len(A) - 1
    while start <= end:
        if not count == 0 or count == 1:
            return
        if start == n or end == n:
            return
        mid = (start + end) // 2
        if n > arr[mid]:
            start = mid
            if check:
                check -= 1
            else:
                check += 1
        elif n < arr[mid]:
            end = mid
            if check:
                check -= 1
            else:
                check += 1
        else:
            count += 1
            print('찾음')
            return

    return

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    count = 0
    check = 0
    for i in range(M):
        print(B[i], count, check)
        binary(B[i], A)

    print(f'#{tc} {count}')