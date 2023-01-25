def de_identify(num):

    # number = num[0:6]
    # return (str(number) + '*' *7 )

    number = str(num) # 입력된 값을 문자열로 변환
    # replace 메서드로 6번째부터 끝자리까지 * 7개로 대체
    number = number.replace(number[6:], '*' * 7)
    return number

# A. 입력예시
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123*******