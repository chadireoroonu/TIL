t = int(input())

for tc in range(t):
    ox = input()

    score = 0
    score_list = []
    for i in range(len(ox)):
        if ox[i] == 'O':
            score += 1
            score_list.append(score)
        else:
            score = 0

    result = 0
    for i in score_list:
        result += i

    print(result)