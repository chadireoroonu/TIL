dice = list(map(int, input().split()))

counting = 0
num = 0
dice = sorted(dice)
for i in range(len(dice)-1):
    if dice[i] == dice[i+1]:
        counting += 1
        num = dice[i]

if counting == 2:
    print(10000 + num * 1000)
elif counting == 1:
    print(1000 + num * 100)
else:
    num = 0
    for i in dice:
        if i > num:
            num = i
    print(num * 100)