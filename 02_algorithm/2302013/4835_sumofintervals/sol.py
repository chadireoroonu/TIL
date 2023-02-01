import sys # 나중에 여기 두 줄은 빼고 제출하기
sys.stdin = open('input.txt')

T = int(input()) # 처음 주어지는 숫자는 테스트 케이스

for tc in range(1, T+1): # 테스트 케이스 숫자 동안에
    option = list(map(int, input().split())) # 다음 줄의 인자를 리스트로 받음
    N = option[0] # 문제에서 주어진 대로 리스트의 첫 글자는 숫자의 갯수
    M = option[1] # 리스트의 두 번째 글자는 더할 숫자
    num = list(map(int, input().split())) # 그 다음줄은 숫자 리스트로 받음
    sum_list = [] # 합한 숫자들을 담을 빈 리스트 생성
    for i in range(0, len(num)-M+1): # i의 길이가 0부터 전체 num의 길이-M 전까지로 설정해서 범위를 벗어나지 않도록 함
        sum_case = 0 # 숫자들의 합계는 0
        for j in range(i, i+M): # j는 i부터 i+M 전까지
            sum_case += num[j] # 합계에 num[j]를 합산
        sum_list.append(sum_case) # 더한 값을 썸 케이스 리스트에 추가

    sum_max = sum_list[0] # 최댓값과 최솟값은 썸 케이스 리스트의 첫 인자로 설정
    sum_min = sum_list[0]

    for k in sum_list: # k가 썸리스트 안에 있는 동안
        if k < sum_min: # k가 최솟값보다 작다면 최솟값 갱신
            sum_min = k
        if k > sum_max: # k가 최댓값보다 크다면 최댓값 갱신
            sum_max = k

    print(f'#{tc} {sum_max - sum_min}') # 출력 예시에 맞게 결과물 출력



