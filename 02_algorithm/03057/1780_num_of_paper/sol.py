import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt_minus = 0
cnt_zero = 0
cnt_plus = 0

# 종이의 숫자가 같은지 판별
def num(arr, n):
    global cnt_minus
    global cnt_zero
    global cnt_plus
    minus = True
    zero = True
    plus = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                zero = False
                plus = False
            elif arr[i][j] == 0:
                minus = False
                plus = False
            elif arr[i][j] == 1:
                minus = False
                zero = False
    if minus == True:
        cnt_minus += 1
    elif zero == True:
        cnt_zero += 1
    elif plus == True:
        cnt_plus += 1
    else:
        cutting(arr, n)

def cutting(arr, n):
    di = [0, n//3, 0, n//3, 0, n//3, n//3, 2*n//3, n//3, 2*n//3, n//3, 2*n//3, 2*n//3, n, 2*n//3, n, 2*n//3, n]
    dj = [0, n//3, n//3, 2*n//3, 2*n//3, n, 0, n//3, n//3, 2*n//3, 2*n//3, n, 0, n//3, n//3, 2*n//3, 2*n//3, n]
    for k in range(9):
        new_paper = []
        for i in range(di[k*2], di[k*2+1]):
            temp = []
            for j in range(dj[k*2], dj[k*2+1]):
                temp.append(arr[i][j])
            new_paper.append(temp)

        num(new_paper, n//3)

num(paper, n)

print(cnt_minus)
print(cnt_zero)
print(cnt_plus)