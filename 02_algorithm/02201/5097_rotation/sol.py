import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    # 주어진 횟수 m 동안 queue의 맨 앞 요소를 마지막에 붙여넣기 반복
    for i in range(m):
        queue.append(queue.pop(0))
    # 반복이 끝난 후, 가장 앞에 있는 요소 출력
    print(f'#{tc} {queue.pop(0)}')