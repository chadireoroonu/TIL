import sys
sys.stdin = open('input.txt')

# 중위순회 방식으로 word 글자 출력
def words(node):
    if node:
        words(left[node])
        print(word[node], end= '')
        words(right[node])

# 문자열을 저장하기 위한 word 리스트 추가로 생성
for tc in range(1, 11):
    n = int(input())
    parent = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    word = [0] * (n + 1)

    # 입력되는 문자열이 네개 이하라면, 자식들을 입력 하지 않고 패스
    for i in range(n):
        temp = list(map(str, input().split()))
        word[int(temp[0])] = temp[1]
        try:
            left[int(temp[0])] = int(temp[2])
        except:
            pass
        try:
            right[int(temp[0])] = int(temp[3])
        except:
            pass
        parent[int(temp[0])] = int(temp[0])

    # 함수를 호출한 뒤 프린트
    print(f'#{tc}', end= ' ')
    words(1)
    print()
