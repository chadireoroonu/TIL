import sys
sys.stdin = open('input.txt')

def find(arr, n, m, k):
    if k > n:
        for i in range(n):
            for j in range(m-k+1):
                ground = ''
                for k in range(k):
                    ground += arr[i][j+k]
                if len(ground) == n:
                    return n
                else:
                    return find(arr, n, m, k-1)




t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for w in range(n)]
    if n > m:
        new_arr = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(arr[j][i])
            new_arr.append(temp)
        arr = new_arr
        n, m = m, n
        k = m
    # print(arr)
    print(find(arr, n, m, k))