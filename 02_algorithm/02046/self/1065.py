n = int(input())

def solve(n):
    counting = 0
    for i in range(1, n+1):
        # i_list = []
        # while True:
        #     if i % 10 != 0:
        #         i_list.append(i % 10)
        #         i = i // 10
        #     else:
        #         break
        if i < 10:
            counting += 1
        else:
            i_list = list(map(str, str(i)))
            sub = []
            for i in range(len(i_list)-1):
                temp = int(i_list[i]) - int(i_list[i+1])
                if temp not in sub:
                    sub.append(temp)
            if len(sub) == 1:
                counting += 1

    return print(counting)

solve(n)