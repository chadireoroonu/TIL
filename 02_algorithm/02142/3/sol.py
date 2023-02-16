import sys
sys.stdin = open('input.txt')
# v = voltex = 노드
# e = edge = 간선

# 조사를 시작하는 노드의 번호를 인자로 넣음
def DFS(start): # 문제에서는 1번 노드를 제시
    stack = [start] # 시작 지점을 넣고 시작
    visited = [0] * (v+1) # 이전에 방문한 곳을 다시 가지 않도록 하기 위한 확인용
    while stack: # 스택에 값이 있는 동안 조사를 진행
        start = stack.pop() # 다음 조사 대상 꺼내기

        # 방문 표시
        # 이전에 방문한 적이 없다면 방문할 것
        if visited[start] == 0:
            visited[start] = 1
            print(start, end= ' ')
            # 현재 위치 start를 기준으로,
            # 0부터 v+1번 노드까지 모두 조사 가능한지 탐색
            for next in range(1, v+1):
                # start에서 next로 이동 가능하고 next에 방문한 적이 없다면
                if matrix[start][next] == 1 and visited[next] == 0:
                    # 다음 조사 대상에 next를 넣음
                    stack.append(next)

v, e = map(int, input().split())
data = list(map(int, input().split()))

# 이동가능 정보 3차원 리스트
# 7번 노드의 정보를 담기 위한 7번째 인덱스가 필요
matrix = [[0]*(v+1) for _ in range(v+1)]
for i in range(v+1):
    print(matrix[i])

for i in range(e): # 모든 간선의 길이만큼
    '''
    matrix[1][2] = 1
    matrix[2][1] = 1
    이동 가능 정보를 담은 matrix의 인덱스는
    각 노드 번호를 의미한다.
    간선 정보 data의 0번째 -> 첫 번째 출발 노드
    간선 정보 data의 1번째 -> 첫 번째 도착 노드
    
    matrix[data[0]][data[1]] = 1
    matrix[data[1]][data[0]] = 1
    '''
    matrix[data[i * 2]][data[i * 2 + 1]] = 1
    matrix[data[i * 2 + 1]][data[i * 2]] = 1
print()
for i in range(v+1):
    print(matrix[i])

DFS(1)