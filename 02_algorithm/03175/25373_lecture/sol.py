import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())

if n > 28:
    if n / 7 - n // 7:
        print(n//7 + 4)
    else:
        print(n//7 + 3)
else:
    for i in range(1, 8):
        if n <= sum(range(1, i+1)):
            print(i)