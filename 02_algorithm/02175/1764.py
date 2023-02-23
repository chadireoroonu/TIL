import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
listen = [sys.stdin.readline().strip() for i in range(n)]

result = []
for j in range(m):
    temp = sys.stdin.readline().strip()
    if temp in listen:
        result.append(temp)

result = sorted(result)
print(len(result))
for i in result:
    print(i)