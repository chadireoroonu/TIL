import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    ox = input()
    score = 1
    total = 0
    for i in ox:
        if i == 'O':
            total += score
            score += 1
        else:
            score = 1

    print(total)