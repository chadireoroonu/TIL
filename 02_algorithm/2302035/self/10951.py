import sys
sys.stdin = open('input.txt')

while True:
    try:
        a, b = list(map(int, input().split()))
        print(a + b)
    except:
        pass