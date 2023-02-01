# SW Expert Academy 4838
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys # 나중에 여기 두 줄은 빼고 제출하기
sys.stdin = open('input.txt')

T = int(input()) # 처음 주어지는 숫자는 테스트 케이스

for tc in range(1, T+1): # 테스트 케이스의 숫자 동안에
    N = int(input()) # 다음 줄의 인자를 갯수 N으로 설정
    num = list(map(int, input().split())) # 그 다음 줄은 숫자 리스트로 변환
    max_num = num[0] # 리스트의 첫 숫자를 최댓값 및 최솟값으로 설정
    min_num = num[0]
    for j in num: # j가 넘버 리스트를 순회하며,
        if j > max_num: # j가 최댓값보다 크다면 최댓값을 j로 변경
            max_num = j
        if j < min_num: # j가 최솟값보다 작다면 최솟값을 j로 변경
            min_num = j
    print(f'#{tc} {max_num - min_num}') # 출력 예시에 맞는 출력 방식 입력
