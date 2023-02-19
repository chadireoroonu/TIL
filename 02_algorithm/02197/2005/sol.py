import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 파스칼 삼각형을 그리기 위해 n*n 크기의 빈 arr 생성
    arr = [[0] * n for _ in range(n)]

    # 모든 i에 대하여 j가 0일 때는 1의 값 저장
    # j의 범위는 1부터 n까지로 설정한 뒤
    # 각 자리의 값은 해당 좌표 위 왼쪽 좌표 값과
    # 바로 위 좌표 값을 합산하여 할당
    for i in range(n):
        arr[i][0] = 1
        for j in range(1, n):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # arr 순회하며 값이 0이 아닌 경우 출력
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end= ' ')
        print()
