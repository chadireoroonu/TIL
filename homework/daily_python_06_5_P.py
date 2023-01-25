# 반복문 미사용
def sum_of_digit(n):
    num = [] # n의 각 요소를 담을 빈 리스트 생성
    num.extend(str(n)) # 각 요소를 문자열로 바꿔서 num에 할당
    number = list(map(int, num)) # 새 리스트에 각 요소를 숫자로 바꿔서 담기
    return print(sum(number)) # 숫자 리스트의 값 합산

# 반복문 사용
def sum_of_digit(n):
    num = [] # n의 각 요소를 담을 빈 리스트 생성
    num.extend(str(n)) # 각 요소를 문자열로 바꿔서 num에 할당
    number = [] # 숫자열을 담을 빈 리스트 생성
    for i in range(len(num)): # i가 num의 길이 안에 있는 동안
        number.append(int(num[i])) # number 리스트에 숫자 num[i] 추가
    # 숫자들로 구성된 number의 합을 프린트해서 반환
    return print(sum(number))


sum_of_digit(3904) # 16