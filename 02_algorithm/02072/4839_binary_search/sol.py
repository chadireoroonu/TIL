import sys
sys.stdin = open('input.txt')

# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면,
# 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고,
# 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

# 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때,
# 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오.
# 비긴 경우는 0을 출력한다.

t = int(input())

# 문제에서 주어진 테스트 케이스 동안 반복을 진행한다.
# 다음 줄의 첫 인자는 책의 전체 페이지 이며,
# 그 다음은 각각 a와 b가 찾을 페이지를 의미한다.
for tc in range(1, t+1):
    r, a, b = list(map(int, input().split()))

    # 책의 범위는 시작 페이지 1부터
    # 책의 총 페이지 r까지 이다.
    start = 1
    end = r

    # a의 반복 횟수를 찾기 위해서 이진탐색을 진행한다.
    # 탐색 동안 초기 설정한 start와 end를 변경해주며
    # 각 과정을 거칠때마다 count_a를 +1 해준다.
    count_a = 0
    while start <= end:
        if (start + end) // 2 == a:
            count_a += 1
            break
        elif (start + end) // 2 > a:
            end = (start + end) // 2
            count_a += 1
        else:
            start = (start + end) // 2
            count_a += 1

    # b의 반복 횟수를 찾기 위해서 이진탐색을 진행한다.
    # 시작 전, 책의 범위를 다시 1부터 r까지로 초기화한다.
    # 탐색 동안 초기 설정한 start와 end를 변경해주며
    # 각 과정을 거칠때마다 count_b를 +1 해준다.

    start = 1
    end = r

    count_b = 0
    while start <= end:
        if (start + end) // 2 == b:
            count_b += 1
            break
        elif (start + end) // 2 > b:
            end = (start + end) // 2
            count_b += 1
        else:
            start = (start + end) // 2
            count_b += 1

    # 반복을 끝낸 후, 카운트 값을 비교하여
    # 카운트 횟수가 적은 사람을 승자로 출력하며,
    # 횟수가 같은 경우에는 0을 출력한다.
    if count_a < count_b:
        print(f'#{tc} A')
    elif count_a > count_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')