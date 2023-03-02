import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    w = input()
    word = input()

    count = 0
    for i in w:
        temp = word.count(i)
        if temp > count:
            count = temp

    print(f'#{tc} {count}')