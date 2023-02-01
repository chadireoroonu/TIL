import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    weith = int(input())
    build = list(map(int, input().split()))

    house = 0
    for i in range(0, len(build)-1):
        home = []
        if build[i] - build[i-1] >= 2:
            home.append(build[i] - build[i-1])
            if build[i] - build[i-2] >= 2:
                home.append(build[i] - build[i-2])
                if build[i] - build[i+1] >= 2:
                    home.append(build[i] - build[i+1])
                    if build[i] - build[i+2] >= 2:
                        home.append(build[i] - build[i+2])

        if len(home) == 4:
            min_num = home[0]
            for j in home:
                if j < min_num:
                    min_num = j
            house += min_num

    print(house)