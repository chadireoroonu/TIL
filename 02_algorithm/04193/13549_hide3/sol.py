# 수빈이의 좌표와 동생의 좌표가 같다면 0 출력, 다르다면 함수 실행
# BFS 함수로 가능한 모든 좌표 visited 배열 생성 후 방문 표시
# 시간초과 방지를 위해 queue + pointer 사용
# 시간을 덜 소모하는 순간이동을 걷기보다 우선 배치하여 먼저 방문 처리
# 순간이동과 걷기를 분리하여 visited 시간 기록
# 수빈이의 좌표가 동생과 같아지면 visited 값 -1 출력 반환

import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

def find(num):
    visited = [0] * 100001    # 최대 숫자 배열 생성
    queue = [num]
    visited[num] = 1
    p = 0    # 시간초과 방지 포인터 사용
    while p < len(queue):
        i = queue[p]
        p += 1
        di = [i, -1, 1]    # i 우선 이동
        for j in range(3):
            ni = i + di[j]
            if 0 <= ni < 100001 and visited[ni] == 0:
                if j > 0:    # 걷는 경우
                    visited[ni] = visited[i] + 1
                elif j == 0:    # 순간이동
                    visited[ni] = visited[i]
                queue.append(ni)
                if ni == K:
                    return print(visited[ni]-1)
if N == K:
    print(0)
else:
    find(N)