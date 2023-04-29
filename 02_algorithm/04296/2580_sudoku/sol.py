# 채워야할 좌표들을 넣은 queue 생성
# queue 있는 동안 반복
# 함수로 가로열, 세로열, 인근 9개 칸의 딕셔너리 채우기 -> 얕은 복사 주의
# 없는 값으로 0 재할당
#

import sys
sys.stdin = open('input.txt')

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

sudoku = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

