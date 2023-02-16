def powerset(arr, k, result):
    global count
    if sum(result) > 10:
        return 
    count += 1
    if k == len(arr):
        # 모든 result를 반환하지는 않을 예정
        if sum(result) == 10:
            print(result)
        return
    # k는 아무튼 증가하는데
    # k번째를 쓴 경우
    powerset(arr, k + 1, result + [arr[k]])
    # k번째를 안 쓴 경우
    powerset(arr, k + 1, result)

arr = list(range(1, 11))
count = 0

# 원본 배열, 사용한 원소 수, 총합 리스트(사용할 원소를 담을 것)
powerset(arr, 0, [])