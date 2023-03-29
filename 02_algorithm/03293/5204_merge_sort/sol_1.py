
import sys
sys.stdin = open('input.txt')

# 제한시간 초과 오답
# 8 / 10 테스트 케이스 정답
def merge_sort(arr):    # 병합 정렬 left, right 정렬
    if len(arr) == 1:    # 최소 단위로 쪼갰다면 반환
        return arr
    # arr 길이를 반으로 나눈 곳을 기준으로,
    # left, right 리스트 채움
    left, right = [], []
    mid = len(arr) // 2
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])

    # left, right 정렬을 위한 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 정렬된 두 리스트로 다음 병합 함수 실행
    return merge(left, right)

def merge(left, right):
    global count
    result = []

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
    if left[-1] > right[-1]:
        count += 1

    # 두 리스트에 남는 요소가 없을 때까지 반복
    # 두 요소의 첫 자리를 비교하며 작은 수 pop
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 한쪽만 요소가 남았다면 모두 result 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    count = 0

    # 병합 정렬 결과 저장
    num = merge_sort(num)

    print(f'#{tc} {num[N//2]} {count}')