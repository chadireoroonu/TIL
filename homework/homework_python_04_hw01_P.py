words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

i = 0
alpha = []
while True:
    if words[[i][-1]] != words[[i+1][0]]:
        break
    else:
        if words[i] in alpha:
            break
        else:
            alpha.append(words[i])
            pass
    i += 1

print(f'{[i+1]} lose')


# for i in words:
#     if i([-1]) == i+1([0]):
#         pass # 단어의 마지막 글자와 다음 단어의 시작 글자가 같다면 패스
#     else: # 단어의 마지막 글자가 다음 단어 시작 글자가 같지 않다면 패배
#         print(f'{i+1} lose')

# alpha = []
# i = 0
# for word in words:
#     if words[[i][-1]] != words[[i+1][0]]: 
#         print(f'{words[i+1]} lose')
#     else:
#         if words[i] in alpha:
#             print(f'{words[i+1]} lose')
#         else:
#             alpha.append(words[i])
#     i += 1

# alpha = []
# i = 0
# while i > range(len(words)):
#     if words[[i][-1]] != words[[i+1][0]]:
#         print(f'{words[i+1]} lose')
#     else:
#         if words[i] in alpha:
#             print(f'{words[i+1]} lose')
#         else:
#             alpha.append(words[i])
#     i += 1
