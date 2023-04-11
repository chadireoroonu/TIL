import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
word = [''] * n
count = 0

for i in range(n):
    temp = sys.stdin.readline().strip()
    word[i] = temp

for i in range(m):
    temp = sys.stdin.readline().strip()
    if temp in word:
        count += 1

print(count)