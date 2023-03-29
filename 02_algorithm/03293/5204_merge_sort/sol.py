import sys
sys.stdin = open('input.txt')

def merge_sort(arr):    # 병합 정렬 left, right 정렬
    if len(arr) < 2:    # 최소 단위로 쪼갰다면 반환
        return arr
    # arr 길이를 반으로 나눈 곳을 기준으로,
    # left, right 리스트 채움
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

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
    i = 0
    j = 0
    # 두 리스트의 모든 요소가 result 추가 시 종료
    # i, j 인덱스로 비교하며 두 리스트 인덱스 값 중 작은 값 추가
    # 값을 추가한 리스트의 인덱스 + 1
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 한쪽만 요소가 남았다면 모두 result 추가
        elif len(left) > i:
            result.append(left[i])
            i += 1
        elif len(right) > j:
            result.append(right[j])
            j += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    count = 0

    # 병합 정렬 결과 저장
    num = merge_sort(num)

    print(f'#{tc} {num[N//2]} {count}')
