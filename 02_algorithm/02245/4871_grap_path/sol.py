import sys
sys.stdin = open('input.txt')

# 출발지, 도착지 연결 여부를 알기 위한 함수 생성
def path(arr, s):
    stack = [s]
    # 스택이 있는 동안 반복
    # 만약 지금 뽑아낸 요소가 g 라면 1 반환
    while stack:
        now = stack.pop()
        if now == g:
            return 1
        # 아니라면, 1~v+1 범위 동안
        # now 연결된 길 스택에 추가
        for shift in range(1, v+1):
            if arr[now][shift] == 1:
                stack.append(shift)
    # 최종 미반환 시 0 반환
    return 0

T = int(input())
for tc in range(1, T+1):
    v, e = list(map(int, input().split()))
    # 0 미사용 -> v+1 * v+1 배열 생성
    # 시작점, 도착점 정보 입력받아 arr 저장
    arr = [[0] * (v+1) for _ in range(v+1)]
    for ec in range(e):
        start, end = list(map(int, input().split()))
        arr[start][end] = 1
    s, g = list(map(int, input().split()))

    # 함수에 arr, s 넣어 출력
    print(f'#{tc} {path(arr, s)}')
