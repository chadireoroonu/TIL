import sys
sys.stdin = open('input.txt')

n = int(input())
for q in range(0, n):
    num_list = []
    num = input()
    for i in range(len(num)):
        num_list.append(num[i])
    num_list = list(map(int, num_list))
    counting_arr = [0] * 9
    for i in num_list:
        counting_arr[i-1] += 1

    print(counting_arr)

    baby_gin = []
    # for i in counting_arr:
    #     if i == 6:
    #         baby_gin.append(2)
    #     elif i == 3:
    #         baby_gin.append(1)
    # print(baby_gin)
    sum_list = []
    for i in range(0, 4):
        sum_case = 0
        for j in (0, 3):
            if counting_arr[j] == 1:
                sum_case += counting_arr[j]
        # if sum_case == 3:
        #     baby_gin.append(1)
        # elif sum_case == 6:
        #     baby_gin.append(2)

    print(baby_gin)

    # if sum(baby_gin) == 2:
    #     print(f'#{q+1} 1')
    # else:
    #     print(f'#{q+1} 0')

    # print(counting_arr)
    # print(num_list)