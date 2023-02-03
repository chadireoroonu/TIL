# https://www.acmicpc.net/problem/2566
import sys
sys.stdin = open('input.txt')

num = []
for k in range(0, 9):
    n = list(map(int, input().split()))
    num.append(n)

max_num = num[0][0]
i_index = 0
j_index = 0
for i in range(9):
    for j in range(9):
        if num[i][j] > max_num:
            max_num = num[i][j]
            i_index = i
            j_index = j
        else:
            pass

print(max_num)
print(f'{i_index+1} {j_index+1}')