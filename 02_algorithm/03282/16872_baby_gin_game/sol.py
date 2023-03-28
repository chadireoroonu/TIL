import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input()))

    # triplest 찾아서 제거
    for i in range(10):
        temp = 0
        for j in range(len(num)):
            if i == num[j]:
                temp += 1
        if temp == 6:
            for k in range(6):
                num.remove(i)
        if temp == 3:
            for k in range(3):
                num.remove(i)


    # num 있다면 정렬
    if num:
        for i in range(len(num)):
            mini = num[i]
            idx = i
            for j in range(i, len(num)):
                if num[j] < mini:
                    mini = num[j]
                    idx = j
            num[i], num[idx] = mini, num[i]

        # run 찾아서 제거
        for i in range(len(num)):
            runnig = []
            start = i
            for j in range(start+1, len(num)):
                if num[start] + 1 == num[j]:
                    if runnig:
                        runnig.append(num[j])
                    else:
                        runnig.append(num[start])
                        runnig.append(num[j])
                    start = j
            if len(runnig) == 3:
                for k in runnig:
                    num.remove(k)

        # run 최대 2개
        for i in range(len(num)):
            runnig = []
            start = i
            for j in range(start+1, len(num)):
                if num[start] + 1 == num[j]:
                    if runnig:
                        runnig.append(num[j])
                    else:
                        runnig.append(num[start])
                        runnig.append(num[j])
                    start = j
            if len(runnig) == 3:
                for k in runnig:
                    num.remove(k)


    # 남아있는 요소가 없다면 True
    if num:
        print(False)
    else:
        print(True)