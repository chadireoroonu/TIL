words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# words[0][-1] == words[1][0]

# lenth = 0
# for i in words:
#     print(lenth)
#     print(words[lenth][-1] == words[lenth + 1][0])
#     lenth += 1


# 처음부터 words의 길이보다 1 작은 위치를 조회할 때까지 반복
duplicated_word = []
idx = 0
while idx < len(words) -1:
    if words[idx][-1] == words[idx + 1][0] and words[idx] not in duplicated_word:
        duplicated_word += [words[idx]]
    else:
        print(f'{idx+1}번째가 탈락했습니다.')
        break
    idx += 1