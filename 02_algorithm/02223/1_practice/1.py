import sys
sys.stdin = open('input.txt')

def preorder(node):
    # 전위 순회이기 때문에 내가 할 일 먼저 함
    print(noed, end= ' ')
    # 이후 왼쪽 자식 조사
    preorder(left[node])
    # 이후 오른쪽 조사
    preorder(right[node])

v = int(input())
e = v-1
edge = list(map(int, input().split()))

# 인덱스를 활용할 것이기 때문에 노드의 개수 +1
# 0번 노드는 없음
parent = [0] * (v+1)  # 부모의 정보
left = [0] * (v+1)  # 왼쪽 자식 정보
right = [0] * (v+1)  # 오른쪽 자식 정보

tree = [[0] * 3 for _ in range(v+1)]

for i in range(e):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:  # 아직 왼쪽 자식이 없으면
        left[p] = c   # p번의 왼쪽 자식 c
    else:             # 왼쪽 자식이 있으면 오른쪽에 넣기
        right[p] = c
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] == 3
    tree[c][2] == p

print(tree)

root = 0
for i in range(1, v+1):
    if parent[i] == 0:
        root = 1
        break
print(left)
preorder(root)