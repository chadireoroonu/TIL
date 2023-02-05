num = []
for i in range(5):
    num.append(int(input()))

num = sorted(num)
s = len(num)//2

print(int(sum(num)/len(num)))
print(num[s])