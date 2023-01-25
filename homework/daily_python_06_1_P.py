def de_identify(num):

    number = num[0:6]

    return (str(number) + '*' *7 )

# A. 입력예시
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123*******