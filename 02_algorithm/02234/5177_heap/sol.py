import sys
sys.stdin = open('input.txt')


def full(i):
    global temp
    if i and parent[i]:
        full(left[i])
        full(right[i])
        temp += 1
        tree[i] = data[temp]
        if tree[i] > tree[left[i]]:
            tree[i], tree[left[i]] = tree[left[i]], tree[i]
        elif tree[i] > tree[right[i]]:
            tree[i], tree[right[i]] = tree[right[i]], tree[i]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    parent = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)
    data = list(map(int, input().split()))
    temp = -1

    for i in range(1, n):
        left[i] = i * 2
        parent[i] = i
        if i * 2 == n:
            break
        right[i] = i * 2 + 1
        parent[i] = i
        if i * 2 + 1 == n:
            break


    full(1)
    print(tree)
    # print(left)
    # print(right)

    # for i in range(len(data)):
