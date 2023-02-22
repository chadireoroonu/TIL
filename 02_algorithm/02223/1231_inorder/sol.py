import sys
sys.stdin = open('input.txt')

def words(node):
    if node:
        words(left[node])
        if word[left[node]] != 0:
            print(word[left[node]], end= ' ')
        words(right[node])
        # if word[right[node]] != 0:
        #     print(word[right[node]], end= ' ')

for case in range(10):
    n = int(input())
    parent = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    word = [0] * (n + 1)

    for i in range(n):
        temp = list(map(str, input().split()))
        word[int(temp[0])] = temp[1]
        try:
            left[int(temp[0])] = int(temp[2])
        except:
            pass
        try:
            right[int(temp[0])] = int(temp[3])
        except:
            pass
        parent[int(temp[0])] = int(temp[0])


    words(1)
    print()
