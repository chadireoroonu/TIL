import sys
sys.stdin = open('input.txt')

def quick_sort(arr):    # 퀵소트 함수
    if len(arr) <= 1:   # 모든 요소를 쪼개 크기 비교
        return arr
    # arr[0]을 기준으로 크기를 비교하여 왼쪽, 오른쪽 리스트 채우고
    # 재귀호출을 이용해 모든 요소에 대한 정렬 진행
    else:
        pivot = arr[0]
        left, right = [], []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    # 정렬한 새 배열 저장
    num = quick_sort(num)

    # 문제에서 요구한 요소 출력
    print(f'#{tc} {num[N // 2]}')
