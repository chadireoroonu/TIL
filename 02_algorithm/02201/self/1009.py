import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for tc in range(T):
    a, b = list(map(int, sys.stdin.readline().split()))

    times = a
    for i in range(b-1):
        times = str(a * a)[-1]

    print(str(times)[-1])