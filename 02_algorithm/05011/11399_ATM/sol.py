# 소요 시간을 최소화를 위해 배열 정렬
# 정렬한 값들로 누적합 배열 생성
# 누적합 배열의 총합 출력

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
people = list(map(int, sys.stdin.readline().split()))

people.sort()
time = [0] * (N + 1)

for i in range(N):
    time[i+1] = time[i] + people[i]

print(sum(time))