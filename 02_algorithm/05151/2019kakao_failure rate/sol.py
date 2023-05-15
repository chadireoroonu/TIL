# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3

import sys
sys.stdin = open('input.txt')

N = int(input())
stages = list(map(int, input().split()))

def solution(N, stages):
    answer = []
    cnt = []  # 통과 못한 사람
    people = [0] * (N + 1)  # 전체 사람

    for i in range(1, N + 1):
        people[i] = stages.count(i) + people[i-1]
        try:
            cnt.append([stages.count(i) / (len(stages) - people[i-1]), i])
        except:
            cnt.append([0, i])

    cnt.sort(key=lambda x:x[1])
    cnt.sort(key=lambda x:-x[0])

    for i in cnt:
        answer.append(i[1])

    print(answer)

    return answer

solution(N, stages)