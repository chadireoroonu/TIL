import sys
sys.stdin = open('input.txt')

def find(arr, n, m, l):
    maxi = 1
    if l == 1:
        return maxi
    else:
        if l > n:
            for i in range(n+l):
                temp = 0
                for j in range(m):
                    if arr[i][j] == 1:
                        temp += 1
                    else:
                        if temp > maxi:
                            maxi = temp
                        temp = 0
                if temp > maxi:
                    maxi = temp
                if maxi == l:
                    return maxi
            else:
                return find(arr, n, m, k-1)

        else:
            for i in range(n):
                temp = 0
                for j in range(m):
                    if arr[i][j] == 1:
                        temp += 1
                    else:
                        if temp > maxi:
                            maxi = temp
                        temp = 0
                if temp > maxi:
                    maxi = temp
                if maxi == l:
                    return maxi

            for i in range(n):
                temp = 0
                for j in range(m):
                    if arr[j][i] == 1:
                        temp += 1
                    else:
                        if temp > maxi:
                            maxi = temp
                        temp = 0
                if temp > maxi:
                    maxi = temp
                if maxi == l:
                    return maxi
            else:
                return find(arr, n, m, l-1)

t = int(input())
for tc in range(1, t+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    l = m

    print(f'#{tc} {find(arr, n, m, l)}')
