import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(n):
    nic = list(map(str, input().split()))

    nic[0] = 'god'

    result = ''
    for j in nic:
        result += j

    print(result)