import sys
sys.stdin = open('input.txt')

# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만,
# 이번에는 특별한 정렬을 하려고 한다.

# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수,
# 2번째 큰 수, 2번째 작은 수 식으로
# 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5

# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오


# 맨 첫줄에 주어진 테스트 케이스 만큼 반복을 진행한다.
# 테스트 케이스 아랫줄에는 정렬할 숫자의 개수를,
# 그 아랫줄에는 개수만큼의 정렬할 숫자들을 받아준다.
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    # 정렬을 위한 함수를 생성한다.
    # 이때, 인자로는 주어진 숫자들로 이루어진 리스트와
    # 리스트의 길이를 parameter로 집어넣는다.
    def select(num, n):

        # i와 i+1의 숫자를 비교할 것이므로,
        # i의 범위는 전체 길이에서 -1하여 설정하고
        # 최솟값과 최댓값을 i로 설정해준다.
        for i in range(n-1):
            mini = i
            maxi = i
            # 만약 i가 2로 나누어 떨어지지 않는 수라면,
            # 앞에서부터 최솟값을 찾아 바꾸어나가야 한다.
            # j의 범위는 i와 같은 이유로 시작 값을 i+1,
            # 마지막 값을 n으로 설정 한 뒤,
            # 최솟값을 찾아 i의 자리 숫자와 바꾼다.
            if i % 2:
                for j in range(i+1, n):
                    if num[mini] > num[j]:
                        mini = j
                num[i], num[mini] = num[mini], num[i]

            # 만약 i가 2로 나누어 떨어지는 수라면,
            # 앞에서부터 최댓값을 찾아 바꾸어나가야 한다.
            # i+1 부터 n까지의 범위 동안
            # 최댓값을 찾아 바꾸어 나간다.
            else:
                for j in range(i+1, n):
                    if num[maxi] < num[j]:
                        maxi = j
                num[i], num[maxi] = num[maxi], num[i]

        # 최종적으로 바꾼 num을 리턴한다.
        return num

    # 리턴 값을 담은 리스트 new를 생성하고
    # new 안에 있는 요소들을 10개까지
    # 주어진 양식에 맞게 출력한다.
    new = select(num, n)
    print(f'#{tc}', end= ' ')
    for i in range(10):
        print(new[i], end=' ')
    # 다음 케이스 결과를 출력할 때 줄을 바꾸기 위해
    # 프린트를 한 번 더 추가한다.
    print()
