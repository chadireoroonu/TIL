import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T):
n = int(input())
num_list = []
for i in range(n):
    num = list(map(int, input().split()))
    num_list.append(num)

result_list = []
string = ''
result = []
for i in range(n):
    for j in range(n-1, -1, -1):
        string += str(num_list[j][i])
        if len(string) == n:
            result.append(string)
            string = ''
result_list.append(result)

string = ''
result = []
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        string += str(num_list[i][j])
        if len(string) == n:
            result.append(string)
            string = ''
result_list.append(result)

string = ''
result = []
for i in range(n-1, -1, -1):
    for j in range(n):
        string += str(num_list[j][i])
        if len(string) == n:
            result.append(string)
            string = ''
result_list.append(result)

# print(f'{tc}')
for i in range(n):
    for j in range(n):
        print(result_list[i][j])

