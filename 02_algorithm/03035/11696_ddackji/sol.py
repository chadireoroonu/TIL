import sys
sys.stdin = open('input.txt')

def game(a, b):
    objet = [4, 3, 2, 1]    # 그림의 종류

    for k in range(4):
        if a.count(objet[k]) > b.count(objet[k]):
            return print('A')
        elif a.count(objet[k]) < b.count(objet[k]):
            return print('B')
    # 최종 비기면 D 출력
    return print('D')

n = int(sys.stdin.readline())
for nc in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.pop(0)    # 첫 숫자(그림 수) 제거
    b.pop(0)

    game(a, b)