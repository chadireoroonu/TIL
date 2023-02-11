import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    n = input()
    temp = n[0]
    result = temp.upper() + n[1::]
    print(result)