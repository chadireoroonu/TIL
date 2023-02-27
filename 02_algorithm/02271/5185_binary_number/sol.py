import sys
sys.stdin = open('input.txt')

asc = {hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}
print(asc)

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()
    print(N, N16)
