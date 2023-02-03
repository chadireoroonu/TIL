import sys
sys.stdin = open('input.txt')

for tc in range(0, 10): # 테스트 케이스는 총 10개가 주어짐
    dump = int(input()) # 처음 줄에 입력된 값은 덤프할 수 있는 횟수
    box = list(map(int, input().split())) # 그 다음 값들은 각각을 숫자 형태로 변환하여 박스 리스트에 추가
    for i in range(0, dump): # 덤프 할 수 있는 횟수 동안 반복문 설정
        max_box = box[0] # 가장 높은 박스는 박스의 첫 번째 값으로 임시 설정
        min_box = box[0] # 가장 낮은 박스도 박스의 첫 번째 값으로 임시 설정
        max_index = 0 # 최댓값, 최솟값의 인덱스도 첫 번째에서 시작
        min_index = 0
        for i in range(len(box)): # i가 박스 길이 범위에 있는 동안
            if box[i] > max_box: # 만약 박스 i번째 요소가 최댓값 보다 크다면
                max_box = box[i] # 최댓값 갱신
                max_index = i # 최대 인덱스에 해당 인덱스 할당
            if box[i] < min_box: # 만약 박스 i번째 요소가 최솟값 보다 작다면
                min_box = box[i] # 최솟값 갱신
                min_index = i # 최소 인덱스에 해당 인덱스 할당
        if max_box - min_box <= 1: # 만약 박스 최댓값과 최솟값의 차가 1이내라면 반복문 중단
            break
        else:
            box[max_index] -= 1 # 아니라면 최댓값 - 1
            box[min_index] += 1 # 최솟값은 + 1

    max_box = box[0] # 반복문이 끝난 이후에 방금 조정한 값과 동일한 차를 가지고 있는 것들을 찾기 위한 작업으로
    min_box = box[0] # 최댓값과 최솟값, 최대 인덱스와 최소 인덱스를 다시 초기화 해줌
    max_index = 0
    min_index = 0
    for i in range(len(box)): # 박스 길이 범위 안에서
        if box[i] > max_box: # 최댓값과 최솟값을 찾고, 인덱스를 재설정
            max_box = box[i]
            max_index = i
        if box[i] < min_box:
            min_box = box[i]
            min_index = i

    print(f'#{tc+1} {max_box - min_box}') # 주어진 형식에 맞게 출력

