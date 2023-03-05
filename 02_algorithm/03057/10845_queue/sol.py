import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
queue = []
for _ in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    if temp[0] == 'push':
        queue.append(int(temp[1]))
    elif temp[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)