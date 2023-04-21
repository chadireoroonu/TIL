# 부분집합의 합으로 접근
# 무게를 기준으로 상한선을 정해두고 최대 가치 구하기

import sys
sys.stdin = open('input.txt')

n, k = map(int, sys.stdin.readline().split())
bag = [0] * (n)
value = [0] * (n)
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    bag[i] = w
    value[i] = v

print(bag)
print(value)