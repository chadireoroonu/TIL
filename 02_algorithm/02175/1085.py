import sys
sys.stdin = open('input.txt')

x, y, w, h = list(map(int, input().split()))

mini = x
if y < x:
    mini = y
if w - x < mini:
    mini = w - x
if h - y < mini:
    mini = h - y

print(mini)