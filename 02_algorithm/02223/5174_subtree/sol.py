import sys
sys.stdin = open('input.txt')

# 총 자식의 수를 셀 함수 생성
# 자신을 포함하여 세기 위해 count 초기값은 1
def child(node):
    count = 1
    stack = [node]

    # 스택을 이용하여 스택이 있는 동안 반복
    # 스택의 마지막 요소 now 할당 후
    # 왼쪽, 오른쪽 자식 존재한다면, count + 1,
    # 스택에 존재하는 자식을 추가하여
    # 현재 자식을 부모로 둔 다른 자식 조사 반복
    while stack:
        now = stack.pop()
        if left[now] != 0:
            count += 1
            stack.append(left[now])
        if right[now] != 0:
            count += 1
            stack.append(right[now])

    # 최종적으로는 카운트 수 반환
    return count

T = int(input())
for tc in range(1, T+1):
    e, n = list(map(int, input().split()))
    edge = list(map(int, input().split()))
    # v 인풋이 없어서 최댓값으로 대체
    v = max(edge)

    # 부모, 왼쪽과 오른쪽 자식을 나타낼 리스트 생성
    left = [0] * (v+1)
    right = [0] * (v+1)

    # edge 정보에 따라서 리스트에 값 할당
    for i in range(e):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    print(f'#{tc} {child(n)}')