# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = eval(input()) # 리스트로 주어진 입력 값의 각 요소를 분리


# 주어진 리스트를 순회하면서
# 각 문자를 리스트로 바꾸고 정렬해서 같은지 확인
# -> 같은 것들은 키(원래단어)와 밸류(정렬한 것) 쌍으로 리스트에 추가하기

word_list = {}
for i in range(len(words)):
    

print(word_list)
