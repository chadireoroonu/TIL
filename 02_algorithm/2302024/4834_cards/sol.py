import sys # 여기는 지우고 입력하기
sys.stdin = open('input.txt')

T = int(input()) # 처음 주어지는 숫자로 테스트 케이스 인식

for tc in range(1, T+1): # 테스트 케이스는 1부터 T+1번까지
    n = int(input()) # 다음 줄 인자만큼의 숫자를 받음
    counting_arr = [0] * 10 # 0부터 9까지의 숫자가 있으므로 10칸짜리 counting_arr 생성
    num = input() # 그 다음 줄에 주어지는 숫자를 문자열로 받음
    num_list = list(map(int, num)) # 문자열을 한 글자씩 숫자로 변환하여 num_list에 추가
    for i in num_list: # num_list에 숫자가 있다면
        counting_arr[i] += 1 # counting_arr에서 해당 자릿 수 +1

    max_card = counting_arr[0] # counting_arr의 첫 번째 요소를 최댓값으로 설정
    for j in range(len(counting_arr)): # counting_arr의 길이 범위 안에서
        if counting_arr[j] >= max_card: # counting_arr의 j번째 요소가 최댓값보다 크다면
            max_card = counting_arr[j] # 해당 요소로 최댓값 변경
    if counting_arr.count(max_card) == 1: # 만약 최댓값이 하나라면
        print(f'#{tc} {counting_arr.index(max_card)} {max_card}') # 인덱스와 최댓값 출력
    else: # counting_arr 안에 최댓값이 한 개가 아니라면
        max_list = [] # 최댓값들의 인덱스를 담을 빈 리스트 생성
        for i in range(len(counting_arr)): # counting_arr를 순회하며
            if counting_arr[i] == max_card: # 최댓값 요소들을 찾아
                max_list.append(i) # max_list 리스트에 추가하고
        print(f'#{tc} {max_list[-1]} {max_card}') # 그중 가장 큰 인덱스와 최댓값 출력
