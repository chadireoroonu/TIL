import sys
sys.stdin = open('input.txt')

def win(n, card):
    global candidate
    if len(card) == 1:
        candidate.append(card[1])
    elif len(card) >= 2:
        if card[0] == 1:
            if card[1] == 1:
                candidate.remove(card[1])
            elif card[1] == 2:
                candidate.remove(card[0])
            else:
                candidate.remove(card[1])
        elif card[0] == 2:
            if card[1] == 1:
                candidate.remove(card[0])
            elif card[1] == 2:
                candidate.remove(card[1])
            else:
                candidate.remove(card[0])
        elif card[0] == 3:
            if card[1] == 1:
                candidate.remove(card[0])
            elif card[1] == 2:
                candidate.remove(card[1])
            else:
                candidate.remove(card[1])
        return candidate
    else:
        return win(card[:len(card)//2], n//2), win(card[len(card)//2:]+1, n//2+1)



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = list(map(int, input().split()))
    card = list(enumerate(card, start= 1))

    # print(card)

    candidate = []
    for i in range(n):
        candidate.append(card[i])

    win(n, card)
