# 참가자의 인덱스는 0부터 시작
# 밤에 참가자 i 살해 -> R[i][j] 만큼 유죄지수 변화
# 밤에 temp 배열에 유죄지수 복사, 실험해보기
# 낮에 유죄지수 가장 높은 사람 살해 -> 유죄지수 유지
# 밤, 낮 후 day + 1 무엇이 먼저인지는 예제보고 맞추기
# 밤에 죽이는 시민의 순서로 은진이의 생존 일 수 정해짐

import sys
sys.stdin = open('input.txt')


def night():
    global people, count
    count += 1
    idx = 0
    result = people
    # i 살해 유죄지수 시뮬레이션
    for i in range(n):
        if i == ej:
            continue
        temp = people
        for j in range(n):
            temp[j] = people[j] + r[i][j]

        order_ej = 0
        num_ej = temp[ej]
        for j in range(n):
            if temp[j] > num_ej:
                order_ej += 1
        if idx < order_ej:
            idx = order_ej
            result = temp
            result[i] = 0
    people = result
    print(people)
    day()
    return

def day():

    return


n = int(sys.stdin.readline().strip())
people = list(map(int, sys.stdin.readline().split()))
r = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ej = int(sys.stdin.readline().strip())

count = 0
night()
