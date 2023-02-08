import sys
sys.stdin = open('input.txt')

x_list = []
y_list = []
for i in range(3):
    x, y = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)

point_x = []
point_y = []

for i in x_list:
    if i in point_x:
        point_x.remove(i)
    else:
        point_x.append(i)

for i in y_list:
    if i in point_y:
        point_y.remove(i)
    else:
        point_y.append(i)

for i in point_x:
    print(i, end=' ')
for i in point_y:
    print(i)