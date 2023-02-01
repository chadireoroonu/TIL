year = int(input())

# if year % 4 == 0:
#     if year % 100 != 0:
#         if year % 400 == 0:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(True)
# else:
#     print(False)

if year % 400 == 0: # 400의 배수이면 윤년
    print(True)
elif year % 4 == 0: # 4의 배수이면서 100의 배수가 아니면 윤년
    if year % 100 != 0:
        print(True)
    else: # 4의 배수이면서 100의 배수이면 윤년 아님
        print(False)
else: # 두 조건에 해당하지 않으면 윤년 아님
    print(False)