# 01. workshop answer

## problem
### 1. 문자 print
It's SSAFY 9를 출력하는 프로그램을 작성하시오.
```
# 문자열 내부에 작은따옴표가 있어 큰 따옴표, \' 사용
print("It's SSAFY 9")
print('It\'s SSAFY 9')

```

### 2. 숫자 print
458345 + 623576 를 계산하여 출력하는 프로그램을 작성하시오.
```
# 각 변수에 숫자를 입력하여 합을 출력
a = 458345
b = 623576
print(a+b)
```
<!-- ```
풀이
어떠한 값을 반환하는 내용을 모두 expression(표현식)이라고 부른다.
tmp = list(range(5)) -> [0, 1, 2,
tmp = len([1, 2, 3]) -> 3
``` -->


### 3. 변수를 사용해서 데이터 출력하기
두 변수 greeting, month를 사용해서 Hello July를 출력하는 프로그램을 작성하시오.
```
# 두 문자열을 더하고 공백을 추가해 프린트
greeting = 'Hello'
month = 'July'

print(greeting+' '+month)
```

### 4. 문자형의 입력과 출력
입력 받은 문자를 출력하는 프로그램을 작성하시오.
(힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.)
```
# 문자열을 변수 a에 저장하여 프린트
a = str(input())
print(a)
```

<!-- ```
풀이
input()함수는 코드 실행시 사용자가 입력한 값을 그대로 '문자열'로 받아서 반환한다
숫자를 입력하더라도 문자열로 반환한다.
``` -->
