import sys
sys.stdin = open('input.txt')

v = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

parent = [0] * (v+1)
left = [0] * (v+1)
right = [0] * (v+1)
root = postorder[-1]

left[root] = postorder[-3]
right[root] = postorder[-2]

