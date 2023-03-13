import sys
sys.stdin = open('input.txt')

w = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

while p in w:
    if p in w:
        w = w.replace(p, '')

if w:
    print(w)
else:
    print('FRULA')