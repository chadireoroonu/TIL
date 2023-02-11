import sys
sys.stdin = open('input.txt')

n = int(input())
while True:
    m = int(input())
    if m == 0:
        break
    else:
        if m % n:
            print(f'{m} is NOT a multiple of {n}.')
        else:
            print(f'{m} is a multiple of {n}.')