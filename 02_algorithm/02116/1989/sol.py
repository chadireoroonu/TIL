import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    w = input()
    for i in range(len(w)//2):
        if w[i] != w[-i-1]:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')