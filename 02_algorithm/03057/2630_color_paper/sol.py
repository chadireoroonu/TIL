import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
paper = [''.join(list(map(str, sys.stdin.readline().split()))) for _ in range(n)]

cnt_white = 0
cnt_blue = 0

def color(arr, n):
    global cnt_white
    global cnt_blue
    white = True
    blue = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1':
                white = False
            if arr[i][j] == '0':
                blue = False
    if white == True:
        cnt_white += 1
    elif blue == True:
        cnt_blue += 1
    else:
        cutting(arr, n)

def cutting(arr, n):
    di = [0, n//2, 0, n//2, n//2, n, n//2, n]
    dj = [0, n//2, n//2, n, 0, n//2, n//2, n]

    for k in range(4):
        new_paper = []
        for i in range(di[k*2], di[k*2+1]):
            temp = ''
            for j in range(dj[k*2], dj[k*2+1]):
                temp += arr[i][j]
            new_paper.append(temp)

        color(new_paper, n//2)

color(paper, n)

print(cnt_white)
print(cnt_blue)