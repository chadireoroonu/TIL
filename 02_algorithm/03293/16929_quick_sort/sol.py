import sys
sys.stdin = open('input.txt')

T = 3
for tc in range(T):
    num = list(map(int, input().split()))

    # 퀵소트 진행할 함수
    def quick_sort(arr):
        # 가장 작은 단위로 쪼갰다면 그대로 arr 반환
        if len(arr) <= 1:
            return arr
        # 아니라면 피봇 설정,
        # left, right 초기화
        # 피봇보다 작은 수는 left,
        # 피봇보다 큰 수는 right 추가
        else:
            pivot = arr[0]
            left, right = [], []
            for i in range(1, len(arr)):
                if arr[i] > pivot:
                    right.append(arr[i])
                else:
                    left.append(arr[i])
            # 모든 요소 정렬을 위한 재귀호출
            return [*quick_sort(left), pivot, *quick_sort(right)]

    print(*quick_sort(num))