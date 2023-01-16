t = int(input())
a = list(range(1,t+1))

final = []
for i in a:
    b = list(map(int, input().split(' ')))
    c = round(sum(b)/len(b))
    final.append(c)

for i in a:
    print(f"#{i}", final[i-1])