import sys
sys.stdin = open('input.txt')

t = int(input()) # 입력받은 반복 횟수 동안 반복을 진행한다.
for tc in range(1, t+1):
    n = int(input()) # 총 몇 줄의 파스칼 삼각형을 만들 것인지 입력 받는다.
    arr = [[0] * n for q in range(n)] # 입력받은 줄 수에 맞추어 n*n 크기의 빈 배열을 생성한다.
    arr[0][0] = 1 # 파스칼 삼각형의 첫 숫자는 1이므로 arr[0][0]에 1을 입력해준다.
    for i in range(1, n): # 삼각형을 완성하기 위해 다음줄부터 끝줄까지 이하 과정을 진행한다.
        for j in range(n): # 가로의 경우, 첫 인자로 주어진 것이 없어 그냥 전 범위를 대상으로 한다.
            # 만약 왼쪽 위, 오른쪽 위의 숫자가 존재한다면,
            # arr[i][j]는 왼쪽 위와 오른쪽 위의 숫자를 더한 값이 된다.
            # 각 자릿수가 어긋나 있으므로 오른쪽 위는 직전 위로 나타난다.
            if 0 <= arr[i-1][j-1] and 0 <= arr[i-1][j]:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            # 만약 둘 중 한 값이 없다면, 왼쪽 위의 값이 없다.
            # 오른쪽 위의 값이 arr[i][j]의 값이 된다.
            else:
                arr[i][j] = arr[i-1][j]

    # 배열의 전 범위를 순회하며 arr[i][j]가 0이 아니라면,
    # 줄 단위로 공백을 두고 출력한다.
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end= ' ')
        print()
