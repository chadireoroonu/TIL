grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

max = 0
max_list = []
for i in range(len(grain_lst)):
    if grain_lst[i][1] > max:
        max = grain_lst[i][1]
        max_list.append(grain_lst[i][0])

print(max_list[-1])
