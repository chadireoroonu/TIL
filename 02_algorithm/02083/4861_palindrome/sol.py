import sys
sys.stdin = open('input.txt')

# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

# 주어진 테스트 케이스 수 만큼 반복한다.
# 첫 줄에 주어진 테스트 케이스를 받고, 범위를 설정하고
# 다음 줄에 입력되는 행렬의 가로, 세로 크기 n과
# 단어의 길이 m을 입력 받는다.
# 그 다음 줄부터는 n번동안 주어진 문자열을 분리해서
# 리스트에 집어 넣어 각 알파벳이 한 개씩 들어간 n*n 행렬을 만든다.
t = int(input())
for tc in range(1, t+1):
    n, m = list(map(int, input().split()))
    arr = [list(input()) for w in range(n)]

    # 생성한 단어를 담아줄 빈 리스트를 생성한다.
    # 가로 방향으로 총 행렬의 길이 n을 문자열 m 단위로 순회하기 위해
    # j의 범위는 n-m+1로 설정하고,
    # 문자열을 m개씩 추가하여 리스트에 집어 넣는다.
    # 잠시 후 회문 여부를 비교할 때 편의성을 위해서
    # 문자열로 병합하지 않고 요소 한 개씩 집어넣는다.
    words = []
    for i in range(n):
        for j in range(n-m+1):
            word = []
            for k in range(m):
                word.append(arr[i][j+k])
            words.append(word)

    # 세로 방향에 대해서도 동일한 작업을 수행한다.
    for i in range(n-m+1):
        for j in range(n):
            word = []
            for k in range(m):
                word.append(arr[i+k][j])
            words.append(word)

    # 테스트 케이스를 먼저 출력한 후,
    # 만약 words 안에 있는 i와 i를 뒤집은 것이 같다면
    # i 안에 있는 요소들을 모두 붙여서 출력한다.
    # 다음 테스트 케이스 출력 전 공백을 출력해준다.
    print(f'#{tc}', end=' ')
    for i in words:
        if i == i[::-1]:
            for j in i:
                print(j, end= '')
    print()




