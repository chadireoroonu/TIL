import sys
sys.stdin = open('input.txt')

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
        for i in range(len(num)):
            run = []
            start = i
            for j in range(start+1, len(num)):
                if num[start] + 1 == num[j]:
                    if run:
                        run.append(num[j])
                    else:
                        run.append(num[start])
                        run.append(num[j])
                    start = j
            if len(run) == 3:
                for k in run:
                    num.remove(k)

    if num:
        num.sort()
        for i in range(len(num)):
            run = []
            start = i
            for j in range(start+1, len(num)):
                if num[start] + 1 == num[j]:
                    if run:
                        run.append(num[j])
                    else:
                        run.append(num[start])
                        run.append(num[j])
                    start = j
            if len(run) == 3:
                for k in run:
                    num.remove(k)


    # 남아있는 요소가 없다면 True
    if num:
        print(False)
    else:
        print(True)