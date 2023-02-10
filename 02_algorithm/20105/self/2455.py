import sys
sys.stdin = open('input.txt')

maxi = 0
train = 0
for i in range(4):
    a, b = list(map(int, input().split()))
    train -= a
    if train > maxi:
        maxi = train
    train += b
    if train > maxi:
        maxi = train

print(maxi)