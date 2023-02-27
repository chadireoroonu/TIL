import sys
sys.stdin = open('input.txt')

def preorder(node):   # 전위 순회 함수
    if node:
        print(alphabet[node-1], end= '')
        preorder(left[node])
        preorder(right[node])

def inorder(node):    # 중위 순회 함수
    if node:
        inorder(left[node])
        print(alphabet[node-1], end= '')
        inorder(right[node])

def postorder(node):  # 후위 순회 함수
    if node:
        postorder(left[node])
        postorder(right[node])
        print(alphabet[node-1], end= '')

# 입력받은 문자열을 인덱스로 활용하기 위해 알파벳 배열 생성
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n = int(input())
left = [0] * (n+1)
right = [0] * (n+1)
for i in range(1, n+1):
    p, l, r = list(map(str, input().split()))
    # 입력받은 노드를 인덱스로 활용
    # 왼쪽 자식과 오른쪽 자식이 있으면 각각 저장
    idx = alphabet.index(p)+1
    try:
        left[idx] = alphabet.index(l)+1
    except:
        pass
    try:
        right[idx] = alphabet.index(r)+1
    except:
        pass

preorder(1)
print()
inorder(1)
print()
postorder(1)
