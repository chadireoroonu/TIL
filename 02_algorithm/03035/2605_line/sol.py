import sys
sys.stdin = open('input.txt')

n = int(input())
pop_num = list(map(int, input().split()))

result = []
for i in range(n):
    result.insert(i - pop_num[i], i+1)

print(*result)