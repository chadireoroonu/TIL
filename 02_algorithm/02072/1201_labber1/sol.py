import sys
sys.stdin = open('input.txt')

for q in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for m in range(100)]

    goal = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                goal = j
    # print(goal)

    def labber(iidx, jidx):
        if iidx == 0:
            return jidx
        else:
            for i in range(iidx, 0, -1):
                if jidx == 99:
                    if arr[i][jidx - 1] == 1:
                        iidx = i
                        break
                elif jidx == 0:
                    if arr[i][jidx + 1] == 1:
                        iidx = i
                        break
                elif arr[i][jidx - 1] == 1 or arr[i][jidx + 1] == 1:
                    iidx = i
                    break

            if arr[iidx][jidx - 1] == 1:
                while arr[iidx][jidx-1] == 1:
                    jidx -= 1
            elif arr[iidx][jidx + 1] == 1:
                while arr[iidx][jidx+1] == 1:
                    jidx += 1

                return labber(iidx, jidx)


    print(labber(99, goal))

