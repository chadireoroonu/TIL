import sys
sys.stdin = open('input.txt')

# 최댓값의 인덱스 왼쪽에서 범위를 좁혀나가며
# 새로운 최댓값을 찾고, 총 면적을 더할 함수 생성
def left(arr):
    global total
    global idx
    if arr:
        # 만약 arr 값들의 합이 0이라면, 반복 중단
        while True:
            if sum(arr) == 0:
                return
            # 아니라면, 최댓값과 그 인덱스를 저장하고
            # 총 면적에 최댓값 * (배열길이 - 최댓값 인덱스) 합산
            # 배열의 범위를 좁혀서 반복 작업
            else:
                left_maxi = max(arr)
                left_idx = arr.index(left_maxi)
                total += left_maxi * (len(arr) - left_idx)
                arr = arr[:left_idx]
    return

# 오른쪽도 동일하게 진행
# 슬라이싱 시 최댓값이 들어가지 않도록 유의
def right(arr):
    global total
    global idx
    if arr:
        while True:
            if sum(arr) == 0:
                return
            else:
                right_maxi = max(arr)
                right_idx = arr.index(right_maxi)
                total += right_maxi * (right_idx+1)
                arr = arr[right_idx+1:]
    return

# 주어진 문제에서 최대치가 1000이므로 배열은 1001개로 생성
matrix = [0] * 1001
n = int(sys.stdin.readline())
idx = 0
maxi = 0
total = 0

# 매트릭스에 높이 정보 저장
# 최댓값, 인덱스 저장, 총 면적에 최댓값 저장
for i in range(n):
    w, h = list(map(int, input().split()))
    matrix[w] = h
    if h > maxi:
        maxi = h
        idx = w

total = maxi

# 왼쪽, 오른쪽 함수를 모두 실행 후
# 계산된 총 면적 출력
left(matrix[:idx])
right(matrix[idx+1:])
print(total)





