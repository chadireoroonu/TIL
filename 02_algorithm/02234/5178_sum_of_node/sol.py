import sys
sys.stdin = open('input.txt')

# 왼쪽과 오른쪽 자식 리스트를 생성,
# 트리 리스트를 생성해서 채워줄 예정
T = int(input())
for tc in range(1, T+1):
    n, m, l = list(map(int, input().split()))
    left = [0] * (n+1)
    right = [0] * (n+1)
    tree = [0] * (n+1)

    # 트리에 리프 노드 정보 추가
    for i in range(m):
        no, num = list(map(int, input().split()))
        tree[no] = num

    # 자식 정보 추가 과정
    # 왼쪽 자식에는 i*2 추가
    # 오른쪽 자식에는 i*2+1을 추가
    # 만약 채우는 값이 n이 되면 중단
    for i in range(1, n):
        left[i] = i*2
        if i*2 == n:
            break
        right[i] = i*2+1
        if i*2+1 == n:
            break

    # n-m에서 0까지 거꾸로 순회하며
    # 왼쪽 자식과 오른쪽 자식이 있다면 해당 자리에 자식들의 합 추가
    # 왼쪽 자식만 있다면 해당 자리에 왼쪽 자식 값 추가
    for i in range(n-m, 0, -1):
        if left[i] and right[i]:
            tree[i] = tree[left[i]] + tree[right[i]]
        elif left[i]:
            tree[i] = tree[left[i]]

    print(f'#{tc} {tree[l]}')
