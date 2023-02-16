import sys
sys.stdin = open('input.txt')

# 도식화한 지도에서 A도시에서 B도시로 가는 길이 존재하는지 조사하려고 한다.
# 길 중간 중간에는 최대 2개의 갈림길이 존재하고,
# 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.
# 다음과 같이 길이 주어질 때,
# A도시에서 B도시로 가는 길이 존재하는지 알아내라.

#  - A와 B는 숫자 0과 99으로 고정된다.
#  - 모든 길은 순서쌍으로 나타내어진다.
#  - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.
#  - 단 화살표 방향을 거슬러 돌아갈 수는 없다.

# 출발점은 0, 도착점은 99으로 표현된다.
# 정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며,
# 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.

# 검사를 진행할 함수를 생성한다.
def DFS(start):
    # 스택을 시작지점으로 설정하고 시작한다.
    # 이전에 방문한 곳인지 확인하기 위하여
    # visited 배열을 만들어준다.
    stack = [start]
    visited = [0] * 100
    # stack이 있다면, 반복을 수행한다.
    # 시작 지점은 반복 시작 시, 스택의 마지막 값으로 한다.
    while stack:
        start = stack.pop()
        # 중간에 b 도시에 도착한다면,
        # 더이상 조사하지 않고 1을 출력한다.
        if start == 99:
            return print(f'#{tc} 1')
        # 같은 곳을 다시 방문하지 않도록
        # visited의 스타트를 1로 표시한다.
        if visited[start] == 0:
            visited[start] = 1
            # 스타트 위치에서 next로 이동가능하고, next가 0이라면 이동
            for next in range(1, 100):
                if matrix[start][next] == 1 and visited[next] == 0:
                    # 다음 조사 대상에 next를 추가한다.
                    stack.append(next)

    # 만약 스택이 없다면 0을 반환한다.
    return print(f'#{tc} 0')

# 총 10 번 동안 반복을 진행한다.
for q in range(10):
    # 첫 줄에는 테스트 케이스의 번호와 길의 개수가 주어진다.
    tc, e = list(map(int, input().split()))
    # 다음 줄에는 길의 방향과 정보가 주어진다.
    data = list(map(int, input().split()))
    # 데이터는 100칸 이므로 100*100 매트릭스를 만들어준다.
    matrix = [[0]*(100) for _ in range(100)]
    # 길의 갯수 동안 데이터를 순회하며
    # 각 데이터 목록에서 두개씩 읽어 매트릭스에 길을 표시한다.
    for i in range(e):
        matrix[data[i * 2]][data[i * 2 + 1]] = 1
    # 함수를 호출해 검사한다.
    DFS(0)