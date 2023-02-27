import sys
sys.stdin = open('input.txt')

# 테스트 케이스 10번 동안
# 단어의 길이 n을 입력받고
# 8*8 칸의 arr를 입력 받음
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for q in range(8)]

    # 빈 리스트를 생성하여 n글자 자리 모든 단어를 담아줌
    temp = []
    for i in range(8):          # 가로 방향 i는 8까지
        for j in range(9-n):    # 가로 방향 j는 8-n+1까지
            word = ''           # 빈 문자열을 생성해서
            for k in range(n):  # 만들어지는 n글자 단어를 리스트에 추가
                word += arr[i][j+k]
            temp.append(word)

    for i in range(9-n):        # 세로 방향 i는 8-n+1까지
        for j in range(8):      # 세로 방향 j는 8까지
            word = ''           # 같은 방식으로 temp에 단어 추가
            for k in range(n):
                word += arr[i+k][j]
            temp.append(word)

    count = 0                   # 카운트 0부터 시작하여
    for q in temp:              # temp 안에 있는 요소들이
        if q == q[::-1]:        # 뒤집어도 같다면 카운트 +1
            count += 1
    print(f'#{tc} {count}')