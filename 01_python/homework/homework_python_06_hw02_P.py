# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = eval(input()) # 리스트로 주어진 입력 값의 각 요소를 분리

def group_anagrams(words):
    word_list = {} # 단어를 담을 빈 딕셔너리 생성
    for i in words: 
        word_alphabet = {} # 단어의 알파벳을 저장할 딕셔너리 생성
        for j in i:
            if j in word_alphabet: # 순회 알파벳이 단어 정보에 있다면 숫자 기록
                word_alphabet[j] += 1
            else: # 없다면, 새롭게 숫자 1을 할당
                word_alphabet[j] = 1 
        word_list[i] = word_alphabet # 단어 : 알파벳 쌍을 딕셔너리에 추가

    anagram = [] # 애너그램을 모을 리스트 생성
    for i in words: # 애너그램 리스트 순회
        for ana in anagram: 
            alpha = ana[0]
            if word_list[i] == word_list[alpha]:
                ana.append(i)
                break
        else:
            anagram.append([i])
    return anagram        


print(group_anagrams(words))