import sys
sys.stdin = open('input.txt')

# 바로 제공 가능한지 판별할 함수 생성
def sol(bread, people):
    # 사람 수 길이 동안 bread, people 비교
    # 만약 사람의 초가 작다면 불가능 출력 반환
    # 불가능한 경우가 없다면 가능 출력 반환
    for i in range(len(people)):
        if bread[i] > people[i]:
            return print(f'#{tc} Impossible')
    return print(f'#{tc} Possible')

T = int(input())
for tc in range(1, T+1):
    n, m, k = list(map(int, input().split()))
    people = list(map(int, input().split()))

    # 사람들의 방문 초를 정렬
    people = sorted(people)

    # 빈 리스트를 만들어서 각 붕어빵이 나오는 초 기록
    bread = []
    for j in range(1, n+1):
        for p in range(k):
            bread.append(j * m)

    sol(bread, people)
