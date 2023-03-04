import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    num = list(map(str, sys.stdin.readline().strip()))
    print(int(num[0])+int(num[-1]))