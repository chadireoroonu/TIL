import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input()
    print(cal)
    stack = []
    result = ''
    for char in cal:
        if char in '+-*/()':
