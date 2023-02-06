import sys
sys.stdin = open('input.txt')

# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1,
# 오른쪽 아래 모서리 r2, c2와
# 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
# color = 1 (빨강), color = 2 (파랑)

# 테스트 케이스 동안 반복을 진행한다.
T = int(input())
for tc in range(1, T+1):
    # 색칠되지 않은 10*10칸짜리 빈 행렬을 생성해준다.
    total_arr = []
    for t in range(10):
        total_arr.append([0] * 10)
    # 칠할 영역의 개수 n을 받고
    # 0부터 n-1까지의 범위동안
    # 주어지는 정보를 리스트로 받는다.
    n = int(input())
    for w in range(n):
        square = list(map(int, input().split()))

        # 리스트의 인덱스를 이용하여 각 사각형의 위치를 설정하고
        # 각 사각형에 해당하는 숫자를 빈행렬에 더해준다.
        for i in range(square[0], square[2]+1):
            for j in range(square[1], square[3]+1):
                total_arr[i][j] += square[-1]

    # 카운팅은 0에서부터 시작하고
    # 처음의 행렬을 순회하며
    # 빨간색(1)과 파란색(2)이 더해진
    # 보라색(3) 칸을 찾을 때마다
    # 카운팅은 +1 하며, 형식에 맞추어 출력한다.
    counting = 0
    for a in range(10):
        for b in range(10):
            if total_arr[a][b] == 3:
                counting += 1

    print(f'#{tc} {counting}')