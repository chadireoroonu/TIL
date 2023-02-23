import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
total = 1
for i in range(n):
    total += int(sys.stdin.readline()) - 1

print(total)