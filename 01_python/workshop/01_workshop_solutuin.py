# 문자열 내부에 작은 따옴표가 있어
# 큰 따옴표로 감싸 주었다.
print("It's SSAFY 9")

# escape sequence를 사용하여 
# 작은 따옴표를 작성하였다.
print('It\'s SSAFY 9')

# 어떠한 값을 반환하는 내용을 모두
# expression (표현식) 이라고 부른다.
# tmp = list(range(5)) -> [0, 1, 2, 3, 4]
# tmp = 0 and 1 -> 0
# tmp = len([1, 2, 3]) -> 3
answer = 458345 + 623576
print(answer)

print(458345 + 623576)

greeting = 'Hello'
month = 'July'
print(greeting, month)

print(f'{greeting} {month}')

# 'hello' + ' ' + 'July'
answer = greeting + ' ' + month
print(answer)

# hello 변수에 input() 함수의 반환값을 담는다.
# input() 함수는 코드 실행시 사용자가 입력한 값을 그대로 `문자열`로 받아서 반환한다.
    # 숫자를 입력하더라도 문자열로 반환한다.
hello = input()
hi = input()
# '3' + '2' == '32'
print(hello + hi)
# 문자열을 정수로 형변환 한 후에 계산해야 한다.
hello = int(hello)
hi = int(hi)
print(hello + hi)