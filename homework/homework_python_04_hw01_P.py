words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

i = 0
alpha = [] # 새로운 것들을 추가해줄 빈 리스트 생성
while i < len(words) -1: # 범위가 넘어가는 것을 막기 위해 words의 길이 -1로 길이 조정
    if words[i][-1] != words[i+1][0]: # 단어의 마지막 글자와 다음 단어의 시작 글자가 다르다면 탈락
        print(f'{i+2} lose')
    else:
        if words[i] in alpha: # 이미 리스트에 있는 단어를 말하면 탈락
            print(f'{i+1} lose')
        else:
            alpha.append(words[i]) #리스트에 없는 단어는 추후 검사를 위해 담아줌
            pass
    i += 1

# 5 lose


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
