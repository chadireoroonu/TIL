import sys
sys.stdin = open('input.txt')

for q in range(10):
    tc = int(input())
    n, m = list(map(int, input().split()))

    # result 첫 인자로는 곱해줄 수 n을 하나 할당
    # 이후 m-1번에 걸쳐 result * n 수행
    result = n
    for i in range(m-1):
        result *= n

    print(f'#{tc} {result}')