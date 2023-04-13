import sys
sys.stdin = open('input.txt')

def sol(start, end):
    if start > end:
        return
    temp = end + 1

    for i in range(start + 1, end + 1):
        if num[start] < num[i]:
            temp = i
            break

    sol(start + 1, temp - 1)
    sol(temp, end)
    print(num[start])


num = []
while True:
    try:
        number = int(input())
        num.append(number)
    except:
        break

sol(0, len(num)-1)