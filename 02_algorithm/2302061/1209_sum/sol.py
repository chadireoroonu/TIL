import sys
sys.stdin = open('input.txt')

# 다음 100X100의 2차원 배열이 주어질 때,
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라.

# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고
# 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.


# 총 10개의 테스트 케이스가 주어지므로 범위는 10으로 설정한다.
# 각 테스트 케이스의 첫 줄에 입력된 숫자는 테스트 케이스 번호를 의미한다.
# 이후 주어지는 100줄은 각 줄이 100개씩 행렬의 한 행을 의미한다.
for q in range(10):
    tc = int(input())
    arr = [list(map(int, input().split()))for w in range(100)]

    # 각 행의 합, 열의 합, 대각선의 합을 더해 넣어줄 빈 리스트를 생성한다.
    total_list = []
    # 행렬 전체를 순회하는 동안 각 행의 합을 total에 더하고,
    # 행이 끝날 때 total 값을 리스트에 추가한다.
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        total_list.append(total)

    # 행렬 전체를 순회하는 동안 각 열의 합을 total에 더하고,
    # 열이 끝날 때 total 값을 리스트에 추가한다.
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
        total_list.append(total)

    # 기울기가 음인 대각선의 합을 구하기 위한 조건으로,
    # i와 j가 같다는 조건을 붙여 합을 구해 리스트에 추가한다.
    for i in range(100):
        total = 0
        for j in range(100):
            if i == j:
                total += arr[i][j]
        total_list.append(total)

    # 기울기가 양인 대각선의 합을 구하기 위한 조건으로,
    # i와 j의 합이 100이라는 조건을 붙여 합을 구한 뒤 리스트에 추가한다.
    for i in range(100):
        total = 0
        for j in range(100):
            if i + j == 100:
                total += arr[i][j]
        total_list.append(total)

    # 최종적으로 모든 합을 추가한 리스트를 순회하며
    # 최댓값을 찾아 문제에서 요구한 방식으로 출력한다.
    maxy = total_list[0]
    for a in total_list:
        if a > maxy:
            maxy = a
    print(f'#{tc} {maxy}')