n = int(input())
score = list(map(int, input().split()))

max_score = score[0]
min_score = score[0]
for i in score:
    if i > max_score:
        max_score = i

new_score = []
for i in score:
    i = i / max_score * 100
    new_score.append(i)

sum_score = 0
for i in new_score:
    sum_score += i

print(sum_score/n)