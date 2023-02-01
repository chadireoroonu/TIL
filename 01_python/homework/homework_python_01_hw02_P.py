s = input('숫자를 입력해주세요 : ')

num = list(s) # 문자열을 리스트로 변환

result = 0 
for i in num: # 문자열에 포함된 요소 전부 반복
    result = result + int(i) # 새 결과값에 기존 결과값 합산
    

print(result)