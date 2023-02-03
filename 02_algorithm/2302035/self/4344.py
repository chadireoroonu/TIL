T = int(input())

for tc in range(T):
    lista = list(map(int, input().split()))
    n = lista.pop(0)
    score = lista

    score_sum = 0
    counting = 0
    for i in score:
        score_sum += i
        counting += 1

    average = score_sum/counting

    good_student = 0
    for i in score:
        if i > average:
            good_student += 1

    per = good_student/counting * 100
    student = round(per, 3)
    print(f'{student:.3f}%')
