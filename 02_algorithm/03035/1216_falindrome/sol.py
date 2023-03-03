import sys
sys.stdin = open('input.txt')

def falindrome(arr, n):
    for i in range(100):    # 가로 줄 n 크기 회문 검사
        temp = ''
        for j in range(101-n):
            for k in range(n):
                temp += arr[i][j+k]
            if temp == temp[::-1]:
                return n
            temp = ''

    for j in range(100):    # 세로 줄 n 크기 회문 검사
        temp = ''
        for i in range(101-n):
            for k in range(n):
                temp += arr[i+k][j]
            if temp == temp[::-1]:
                return n
            temp = ''

    return falindrome(arr, n-1)    # 리턴되지 않으면 n-1로 재귀함수 호출

for case in range(10):
    tc = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    print(f'#{tc} {falindrome(arr, 100)}')
