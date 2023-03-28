import sys
sys.stdin = open('input.txt')

n = 1000 - int(sys.stdin.readline().strip())
coin = 0

def change(m, won):
    global n, coin
    while m >= won:
        coin += m // won
        m %= won
        n = m
    return

money = [500, 100, 50, 10, 5, 1]
for c in money:
    change(n, c)

print(coin)