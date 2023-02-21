import sys
sys.stdin = open('input.txt')

def match(start, end):
    if start == end:
        return start
    center = (start + end) // 2
    left = match(start, center)
    right = match(center+1, end)
    # print(left, right, start, end, center)

    if player[left] == player[right]:
        return left
    if player[left] == 1 and player[right] == 2:
        return right
    if player[left] == 1 and player[right] == 3:
        return left
    if player[left] == 2 and player[right] == 1:
        return left
    if player[left] == 2 and player[right] == 3:
        return right
    if player[left] == 3 and player[right] == 1:
        return right
    if player[left] == 3 and player[right] == 2:
        return left

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    player = list(map(int, input().split()))

    print(f'#{tc} {match(0, N-1) + 1}')