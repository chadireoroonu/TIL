import sys
sys.stdin = open('input.txt')

T = int(input())
# 주어진 테스트 케이스 동안 반복문을 순회한다.
# 당근의 갯수를 n에 할당해두고,
# 공백을 사이에 두고 주어지는 당근의 크기를 numbers에 하나씩 넣어준다.
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 문제에서 주어진 최솟값이 1이기 때문에 카운팅과 맥스 카운팅 모두 1에서 출발한다.
    # 첫 번째 당근의 크기를 기준으로 비교를 시작한다.
    counting = 1
    max_counting = 1
    carrot = numbers[0]

    # 두 번째 당근부터 이전 당근과 크기를 비교하여,
    # 이전의 당근보다 크다면 카운팅 + 1 작업과
    # 당근을 현재 크기로 재할당하는 작업을 수행한다.
    for i in range(1, n):
        if numbers[i] > carrot:
            counting += 1
            carrot = numbers[i]

            # 만약 카운팅이 맥스 카운팅보다 크다면
            # 맥스 카운팅의 값을 재할당한다.
            if counting > max_counting:
                max_counting = counting

        # 당근의 크기가 이전보다 커지지 않았다면,
        # 카운팅과 당근을 초기화한다.
        else:
            counting = 1
            carrot = numbers[i]

    # 문제에서 주어진 조건에 맞게 출력한다.
    print(f'#{tc} {max_counting}')