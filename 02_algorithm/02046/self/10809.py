s = input()
alpha = {}
alpha_list = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha_list:
    alpha[i] = -1
num = 0
num_dic = {}
for i in s:
    if i in alpha:
        if alpha[i] != -1:
            pass
        else:
            alpha[i] = num
    num += 1

for i in alpha.values():
    print(i, end= ' ')
