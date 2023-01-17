s = input('숫자를 입력해주세요 : ')
print(s) # 문자열의 각 자리수를 더하라 -> 1 + 2 + 3 + 4
# 문자열 1234를 숫자 1234로 바꾼다음 10씩 나눈 나머지를 더해나간다.

# 문자열을 순회
result = 0
for char in s: # '1' '2' '3' '4'
    # print(char)
    result = result + int(char)
print(result)

# 리스트로 바꾸기
# arr = list(s)
# print(arr)
# for char in arr: # char '1' '2' '3' '4'
#     # 어떤 값을 연산한 후 다시 본인에게 할당할 때에는 할당 연산자를 사용하면 편함
#     result += int(char)
#     # result = result + int(char)
# print(result)

# +a
# map(function, iterable) -> 순회 가능한 요소가 가진 각 값들을 첫 번째로 작성한 함수에 각각 넣어서 실행
print(list(map(int, s)))
print(sum(map(int, s)))

# 문자열 = 변경 불가능
# 문자열이 가지고 있는 함수 중에, join 함수
# 'some str'.join(iterable)
# print('+'.join(s)) # '1234' => '1+2+3+4'
# print(eval('1+2+3+4')) # 문자열을 계산해주는 역할