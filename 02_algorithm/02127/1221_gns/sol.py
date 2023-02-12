import sys
sys.stdin = open('input.txt')

t = int(input())
for q in range(1, t+1):
    tc, n = list(map(str, input().split()))
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR',
           'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    arr = list(map(str, input().split()))

    print(tc)
    for i in num:
        for j in arr:
            if j == i:
                print(i, end= ' ')
    print()