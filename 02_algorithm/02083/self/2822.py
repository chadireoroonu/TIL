score = [20, 30, 50, 48, 33, 66, 0, 64]
# for q in range(8):
#     a = int(input())
#     score.append(a)

enu = []
for i in enumerate(score, start=1):
    enu.append(i)

print(enu)
# print(enu[0][1])

sum_maxi = 0
maxi_list = []
for j in range(5):
    maxi = 0
    idx = 0
    for i in range(len(enu)):
        if enu[i][1] > maxi:
            maxi = enu[i][1]
            idx = i+1
    sum_maxi += maxi
    maxi_list.append(idx)
    

print(maxi_list)