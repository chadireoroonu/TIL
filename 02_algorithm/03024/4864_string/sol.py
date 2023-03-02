import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    w = input()
    word = input()

    if w in word:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')