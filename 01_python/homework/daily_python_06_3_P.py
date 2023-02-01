def count_vowels(word):
    word = str(word) # 입력받은 단어를 문자열로 변환
    vowels = ['a', 'o', 'e', 'i', 'u'] # 모음을 담은 리스트 생성
    sum = 0 # 모음의 합은 0에서 부터 시작
    for k in range(len(vowels)): # 모음열의 범위를 순회하는 동안
        sum += word.count(vowels[k]) # 단어에서 해당 번째 모음을 세서 합산
    
    return print(sum) # 아래 입력에 프린트가 없으므로 프린트를 붙여서 반환


count_vowels('apple') #=> 2
count_vowels('banana') #=> 3