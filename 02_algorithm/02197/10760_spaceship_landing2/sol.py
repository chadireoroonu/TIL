import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 인근 8방향을 조사하기 위하여 왼쪽 위 좌표부터 오른쪽 아래 좌표까지
    # 가운데 좌표를 기준으로 총 8가지 구역의 상대 좌표를 di, dj의 범위로 설정
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 착륙 가능할 지점을 적을 total 변수 선언 후
    # 전 arr를 순회하며 조사를 진행
    total = 0
    for i in range(n):
        for j in range(m):
            # 인근 8방향 중 착륙지보다 낮은 위치의 개수를
            # 조사하기 위한 count 변수 선언 후
            # 착륙지 인근 8방향의 좌표가 존재하고
            # 착륙지 보다 낮은 위치를 가지는 값을 만나면
            # count 값 1 증가
            count = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[i][j] > arr[ni][nj]:
                        count += 1
            # 8방향에 대한 조사를 수행한 뒤,
            # 착륙지보다 낮은 곳이 4곳 이상이라면
            # total 값을 1 증가
            if count >= 4:
                total += 1

    # 최종적으로, 착륙이 가능한 곳의 개수를 출력
    print(f'#{tc} {total}')