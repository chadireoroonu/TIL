import sys
sys.stdin = open('input.txt')

e, f, c = list(map(int, input().split()))

coke = 0
bottle = e + f
while True:
    if bottle / c >= 1:
        coke += bottle // c
        bottle = bottle // c + bottle % c
    else:
        print(coke)
        break
