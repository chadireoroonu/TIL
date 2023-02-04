s = input()
alpha = {}
alpha_list = 'abcdefghijklimopqrstuvwxyz'
for i in alpha_list:
    alpha[i] = -1
for i in s:
    index_s = 0
    if i in alpha:
        index_s =
        alpha[i] = i + 1

for i in alpha.values():
    print(i, end= ' ')
