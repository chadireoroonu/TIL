import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = list(map(int, input().split()))
    subject = list(map(int, input().split()))

    result = 0
    for i in range(k):
        temp = max(subject)  # k 번 제일 높은 과목 추가
        result += temp
        subject.remove(temp)  # 추가한 점수 삭제

    print(f'#{tc} {result}')