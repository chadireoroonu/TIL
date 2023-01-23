# number = int(input())
# range_number = range(1, number+1) #range는 순서가 있는 시퀀스며, 변형불가능한 특징

# for num in range_number:
#     print(num)



# number = int(input())
# for num in range(1, number+1):
#     print(num, end=' ')



# number = int(input())
# for num in range(number, -1, -1): # range 세 번째 자리는 step인자
#     print(num)



# number = int(input())
# for num in range(number, -1, -1):
#     print(num, end=' ')



# number = int(input())
# result = 0 # 값을 초기화하지 않기 위해 반복문 위에 선언
# for num in range(1, number+1):
#     result += num

# print(result) # for 안에 print를 넣으면 결과값을 계속 출력


# solution1
# number = int(input())
# for num in range(1, number+1):
#     print(' '*(number-num)+'*'*num)


# number = int(input())
# for num in range(number):
#     print(num, '첫 번째 반복문')
#     for num in range(number, -1, -1):
#         print(num, '두 번째 반복문')
#     print()


# solutuin2
# number = int(input())
# for star in range(number+1):
#     for space in range(number-star-1, -1, -1):
#         print(' ', end='')
#     print('*'*star)


# number = int(input())
# for i in range(1, number+1):
#     print(i)
#     for j in range(1, number+1):
#         print(i, j)

# arr = [[i for i in range(4)] for j in range(4)]
# print(arr)

# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20]
# ]

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         # print(i, j) # 프린트 값은 각 숫자들의 좌표라고 생각
#         print(arr[i][j])

# 집에가서 순서 다양하게 뽑아보기
# 뒤에서부터, 세로로, 세로 거꾸로 등
# 파이썬 튜터 사이트로도 확인해보기
# 리스트 가로세로 길이가 다르게도 출력

# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20]
# ]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         # print(i, j) # 프린트 값은 각 숫자들의 좌표라고 생각
#         print(arr[i][j])


# numbers = [
#     85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#     51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#     52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]

# num = []
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if numbers[i] < numbers[j]:
#             num.append(numbers[i])
#         else 

# print(num)


# num = []
# for i in len(numbers):
#     for j in range(len(numbers)):
#         if numbers[i] < numbers[j]:
#             num.append(numbers[i])
#         else 

# print(num)

