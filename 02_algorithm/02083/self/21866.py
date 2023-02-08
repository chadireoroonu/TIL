score = list(map(int, input().split()))

total = 0
for i in score:
    total += i

if score[0] > 100 or score[1] > 100:
    print('hacker')
elif score[2] > 200 or score[3] > 200:
    print('hacker')
elif score[4] > 300 or score[5] > 300:
    print('hacker')
elif score[6] > 400 or score[7] > 400 or score[8] > 500:
    print('hacker')
elif total < 100:
    print('none')
else:
    print('draw')