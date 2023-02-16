def solution(arr, k, result):
    # 부분집합의 합이 10인 경우를 찾고 있다.
    if result != 10:
        return

    for i in range(1, k+1):   # 내가 조사한 데까지       # 여기가 핵심!
        if arr[i]:
            print(data[i], end=' ')
    print()

def make_ncandidates(arr, k, N, c):
    c[0] = True        # 쓰는 상황
    c[1] = False       # 안쓰는 상황
    return 2

def backtraking(arr, k, N, result):
    global count
    if result > 10:    # 더이상 유망성 없는 과정을 반복하지 않도록 함
        count += 1
    # 총 합이 10인 경우를 뽑기 위한 계산은 result로 함
    # 후보군 목록
    c = [0] * 2        # 부분집합 원소 쓸지 말지 결정하기 위해 두 개면 됨

    # 현재 조사하는 위치가 최대 조사 상황에 도달할 때까지 조사 진행
    if k == N:
        solution(arr, k, result)   # 값을 도출하는 함수 실행
    else:
        # 아직 사용해야 하는 원소들이 남았다면
        # 사용할 원소 인덱스 1 증가
        k += 1
        # 내가 해당 원소를 쓸지 말지 결정하는 경우의 수 2개
        # 배열, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 수, 후보군 목록 배열
        ncandidates = make_ncandidates(arr, k, N, c)
        for i in range(ncandidates):    # 후보군 수만큼
            arr[k] = c[i]
            if arr[k]: # k번째 원소 쓰기로 했으면
                # 총합에 원본 데이터의 k번째 원소의 값을 더해준다.
                backtraking(arr, k, N, result + data[k])
            else:      # 안쓰기로 했다면
                # 지금 k번째 원소는 안쓸거지만
                # 다음 조사 진행
                # 대신 안쓸거니까 총합에 더하지 않음
                backtraking(arr, k, N, result)

# 백트래킹을 하기 위해서는 유망성 조사를 위한 변수들이 필요
MAXCANDIDATES = 12     # 최대 후보군 수(적당히 큰 수)
NMAX = 12              # 최대 원소 수(적당히 큰 수)

count = 0
data = list(range(11))
arr = [0] * NMAX       # 각 원소를 사용할 것인지 체크할 배열

# 조사 시작
# 체크할 배열, 시작점, 종료지점, 총합 필요

backtraking(arr, 0, 10, 0)