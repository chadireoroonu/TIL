import sys
sys.stdin = open('input.txt')

# def sol(n):
#     start = 0
#     end = n
#
#     while True:
#         mid = (start + end) // 2
#         parent[mid] = mid


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = n

    k = 0
    while m > 0:
        m //= 2
        k += 1

    parent = [0] * (2 ** k)
    left = [0] * (2 ** k)
    right = [0] * (2 ** k)

    # number = []
    # for i in range(n+1):
    #     number.append(i)

    start = 0
    end = n

    mid = (start+end) // 2 + 1
    parent[mid] = mid
    start = n // 2

    print(mid)
    print(parent)
    print(left)
    print(right)