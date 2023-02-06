import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    for i in range(1<<10):
        new_arr = []
        for j in range(1, 11):
            if i & (1<<j):
                new_arr.append(arr[j])

        if len(new_arr) >= 1:
            if sum(new_arr) == 0:
                print(f'#{tc} 1')
                break
    else:
        print(f'#{tc} 0')