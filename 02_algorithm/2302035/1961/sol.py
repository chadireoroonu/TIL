import sys
sys.stdin = open('input.txt')

# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
# 다음 N 줄에는 N x N 행렬이 주어진다.

# 출력의 첫 줄은 '#t'로 시작하고,
# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

T = int(input())
# 첫 줄에 주어지는 테스트 케이스만큼 전체 과정을 반복한다.
# 그 다음 줄에 주어지는 숫자 n의 범위 만큼,
# 아랫 줄의 숫자들을 받고, 각 줄마다 개별 리스트로 만들어서 전체 리스트에 추가한다.
for tc in range(1, T):
    n = int(input())
    num_list = []
    for i in range(n):
        num = list(map(int, input().split()))
        num_list.append(num)

    # 결과 리스트와 임시 빈 리스트를 만들고,
    # string을 빈 문자열로 생성해 둔 뒤 시작하여
    # i가 n 안에 있는 동안
    # 90도 회전을 위해 i는 오름차순으로, j는 내림차순으로 순회하며
    # 넘버 리스트의 [j][i]번째 요소 구해 빈 문자열에 더해나간다.
    result_list = []
    string = ''
    result = []
    for i in range(n):
        for j in range(n-1, -1, -1):
            string += str(num_list[j][i])

            # 만약, 문자열의 길이가 n과 같아졌다면,
            # 이제까지 더한 값을 리스트에 추가하고
            # 문자열을 초기화하여 반복을 계속한다.
            if len(string) == n:
                result.append(string)
                string = ''

    # 반복을 끝낸 수 가지고 있는 요소를 전체 결과 리스트에 담아준다.
    result_list.append(result)

    # 같은 방식으로 진행하되, 180도 회전한 값을 구하기 위하여
    # i와 j 모두 내림차순으로 순회하며 [i][j] 순으로 출력하여
    # 출력값을 문자열에 더하고, 문자열의 길이가 n과 같아졌다면
    # 문자열을 초기화하여 반복을 계속한다.
    # 전체 반복이 끝나면, 값을 결과 리스트에 추가한다.
    string = ''
    result = []
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            string += str(num_list[i][j])
            if len(string) == n:
                result.append(string)
                string = ''
    result_list.append(result)

    # 같은 방식으로 진행하되, 270도 회전한 값을 구하기 위하여
    # i는 내림차순으로, j는 오름차순으로 순회하며 [j][i] 순으로 출력하여
    # 출력값을 문자열에 더하고, 문자열의 길이가 n과 같아졌다면
    # 문자열을 초기화하여 반복을 계속한다.
    # 전체 반복이 끝나면, 값을 결과 리스트에 추가한다.
    string = ''
    result = []
    for i in range(n-1, -1, -1):
        for j in range(n):
            string += str(num_list[j][i])
            if len(string) == n:
                result.append(string)
                string = ''
    result_list.append(result)

    # 문제에서 주어진 조건에 맞게 출력한다.
    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            print(result_list[j][i], end=' ')
        print()

