import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
queue = []
for _ in range(N):
    w = list(sys.stdin.readline().split())
    if w[0] == 'push':
        queue.append(int(w[1]))
    elif w[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif w[0] == 'size':
        print(len(queue))
    elif w[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif w[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif w[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)