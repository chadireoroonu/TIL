import sys
sys.stdin = open('input.txt')

def running(num):
    for x in range(len(num)):
        run = []
        start = x
        for y in range(start + 1, len(num)):
            if num[start] + 1 == num[y]:
                if run:
                    run.append(num[y])
                else:
                    run.append(num[start])
                    run.append(num[y])
                start = y
        if len(run) == 3:
            for k in run:
                num.remove(k)

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().strip()))

    # triplest 찾아서 제거
    for i in range(10):
        temp = num.count(i)
        if temp == 6:
            for j in range(6):
                num.remove(i)
        if temp == 3:
            for j in range(3):
                num.remove(i)

    # run 찾아서 제거
    if num:
        num.sort()
        running(num)
        running(num)


    # 남아있는 요소가 없다면 True
    if num:
        print(False)
    else:
        print(True)