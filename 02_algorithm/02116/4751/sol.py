import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    w = input()
    print('..#' + '...#'*(len(w)-1) + '..')
    print('.#'*2*len(w) + '.')
    for i in range(len(w)):
        print(f'#.{w[i]}.', end= '')
    print('#')
    print('.#'*2*len(w) + '.')
    print('..#' + '...#' * (len(w)-1) + '..')