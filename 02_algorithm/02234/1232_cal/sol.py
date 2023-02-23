import sys
sys.stdin = open('input.txt')

# 트리를 순회하며 연산자를 만나면
# 왼쪽 자식, 오른쪽 자식으로 연산 수행
# 아래부터 계산해서 올라오기 위해 후위 순회
def cal(i):
    if i:
        cal(left[i])
        cal(right[i])
        if left[i] and right[i]:
            if tree[i] == '+':
                tree[i] = int(tree[left[i]]) + int(tree[right[i]])
            elif tree[i] == '-':
                tree[i] = int(tree[left[i]]) - int(tree[right[i]])
            elif tree[i] == '*':
                tree[i] = int(tree[left[i]]) * int(tree[right[i]])
            elif tree[i] == '/':
                tree[i] = int(tree[left[i]]) // int(tree[right[i]])
        else:
            tree[i] = int(tree[i])

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    # 입력값으로 노드와 트리 정보 추가,
    # 자식이 있다면 각각 자식 추가
    for nc in range(n):
        temp = list(map(str, input().split()))
        tree[int(temp[0])] = temp[1]
        try:
            left[int(temp[0])] = int(temp[2])
        except:
            pass
        try:
            right[int(temp[0])] = int(temp[3])
        except:
            pass

    # 함수를 통해 구한 인덱스 1값 출력
    cal(1)
    print(f'#{tc} {tree[1]}')

