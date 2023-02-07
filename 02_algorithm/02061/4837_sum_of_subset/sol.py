import sys
sys.stdin = open('input.txt')

# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

# 해당하는 부분집합이 없는 경우 0을 출력한다.
# 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )


# 모든 집합은 1에서 12까지의 숫자를 가지므로
# 해당 집합을 생성해두고 시작한다.
bit = []
for q in range(1, 13):
    bit.append(q)

# 첫 줄에 입력되는 테스트 케이스 동안 반복을 진행한다.
T = int(input())
for tc in range(1, T+1):
    # 테스트 케이스 동안 집합 원소의 개수 n과 원소의 합 k가 주어진다.
    n, k = list(map(int, input().split()))

    # 첫 번째 조건인 집합 원소의 개수가 n개인 것들을 모아
    # 추가해 줄 빈 리스트를 생성한다.
    all_mini = []

    # 우선, 집합 bit의 모든 부분집합을 구해준다.
    for i in range(1<<12):
        mini = []
        for j in range(12):
            if i & (1<<j):
                mini.append(bit[j])

        # 해당 부분집합들을 대상으로,
        # 길이가 n과 같은지를 조사하고
        # 통과하면 all_mini 리스트에 추가한다.
        num = 0
        for s in mini:
            num += 1
        if num == n:
            all_mini.append(mini)

    # all_mini 리스트에 추가된 부분집합들을 대상으로
    # 카운팅은 0으로 초기 설정하며,
    # 각 부분집합 내부 요소들의 합을 구해서
    # k와 비교하는 작업을 수행한다.
    counting = 0
    for c in all_mini:
        total = 0
        for z in c:
            total += z

        # 만약, 부분집합 요소들의 합이 k와 같다면,
        # 카운팅을 +1 하고 총 카운팅 수를 출력한다.
        if total == k:
            counting += 1

    print(f'#{tc} {counting}')