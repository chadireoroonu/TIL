import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
hip = []
for _ in range(N):
    i = int(sys.stdin.readline().strip())
    if i > 0:
        hip.append(i)
    else:
        if hip:
            print(min(hip))
            hip.remove(min(hip))
        else:
            print(0)
