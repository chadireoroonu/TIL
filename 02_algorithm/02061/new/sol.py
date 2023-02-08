import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T):
    arr = list(map(int, input().split()))
    N = len(arr)

    # 원소 N개의 모든 경우의 수
    # 2 ** N 은 1 << N과 같다
    # 원소의 개수가 3개라고 할때
    # 2 ** 3 == 8
    # 1 << 3 -> 0b1000 -> 8
    # 0001 -> 1을 왼쪽으로 3번 밀면
    # 1000
    for i in range(1<<N): # N = len(10개의 정수)
        result = 0
        # i -> N으로 만들 수 있는 모든 경우의 수
        # 1번째부터 2**n 번째의 경우의 수
        for j in range(N): # j 번째 넣었는지 안넣었는지
            if i & (1<<j):
                result += arr[j]
        if result == 0:
            print(1)
    else:
        print(0)