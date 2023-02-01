# n = int(input()) # 숫자로 입력값을 받기 #10

# num = [] # 약수를 담을 빈 리스트 생성
# i = 1 # 0으로 나눌 수 없으므로, 1부터 시작
# while i <= n: # i가 n보다 작은 수일때, 나누어 떨어지는지 확인
#     if n % i == 0:
#         num.append(i) # n이 i로 나누어 떨어진다면 리스트에 추가
#     else:
#         pass # 아니라면 패스
#     i += 1 # i는 n과 같아질때까지 1씩 증가

# num.sort() # 리스트 오름차순 정렬

# print(num) #1, 2, 5, 10


# # numbers = input()
# numbers = [1, 2, 3, 4, 5]
# # for i in numbers:
# #     num_list.append(i)


# result = 0
# def list_sum(numbers):
#     if i <= range(len(numbers)):
#         return (result + [i])
#     else:
#         pass
    

# print(list_sum(result))


# numbers = [1, 2, 3, 4, 5]

# result = 0
# def list_sum(numbers):
#     for x in range(len(numbers)):
#         return result + x

# print(result)


# numbers = input().split(',') # 입력 값을 ',' 기준으로 분리 # 1, 2, 3, 4, 5
# num = [] # 정수 형태로 값을 담을 빈 리스트 생성
# for i in numbers: # i가 리스트에 있는 동안 빈 리스트에 정수 i 추가
#     num.append(int(i))

# def list_sum(num): 
#     result = 0 # 초기 결과는 0으로 설정
#     for x in num: # x가 정수 리스트에 있다면 이전 결과에 x값을 합산
#         result = result + x

#     return result

# print(list_sum(num)) # 15


# numbers = input().split(',')
# print(numbers)
# num = numbers.values()

# # for i in numbers:
# #     num.append(int(i))

# def dict_list_sum(num):
#     result = 0
#     for x in num:
#         result = result + x

#     return result

# print(dict_list_sum())


