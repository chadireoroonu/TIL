import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
deque = []
for _ in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    if temp[0] == 'push_front':
        deque.insert(0, int(temp[1]))
    elif temp[0] == 'push_back':
        deque.append(int(temp[1]))
    elif temp[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif temp[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(deque))
    elif temp[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
