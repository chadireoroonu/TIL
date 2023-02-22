import sys
sys.stdin = open('input.txt')

arr = [''.join(list(map(str, input().split()))) for _ in range(8)]

total = 0
for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2 and arr[i][j] == 'F':
                total += 1
        else:
            if j % 2 == 0 and arr[i][j] == 'F':
                total += 1

print(total)