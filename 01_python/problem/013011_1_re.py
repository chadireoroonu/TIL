n = int(input())
csse = int(input())
num_list = list(map(int, input().split('')))

new_list = []

for i in range(0, 1000):
    for j in range(len(new_list)):
        if num_list[i] == new_list[j]:
            new_list[j][1] += 1
        else: 
            new_list.append([num_list[i], 0])

print(new_list)
