# 1. name와 age 라는 두개의 argument를 넘기면 각각 이 값을 출력하는 함수를 작성해보세요.
# argument가 2개라면, parameter도 2개
# define function
def func(name, age):
    print(name, age)
    return f'{name}의 나이는 {age}입니다.'

# call function
# func('Viktor', 26)
print(func)

# 2. 두개의 매개변수가 있고, 이 매개변수들을 덧셈하고 뺄셈한 결과를 모두 반환하는 함수를 작성해 보세요.

def calc(x, y):
    add = x + y
    sub = x - y
    return (add, sub)


# 3. 우리 회사 멤버의 이름과 연봉을 출력하는 함수를 만들어보세요.
# 매개변수는 이름과 연봉이 들어가는데, 만약 함수 호출에서 연봉이 누락되면 기본으로 4500이 나오도록 해주세요.

def hr(name, salary=4500): # 매개변수 뒤에 기본값 추가 가능
    print(name, salary)

hr('Viktor', 4000)
hr('Kim')

# 4. n을 넘기면 1부터 n까지 더하는 my_sum 함수를 만들어보세요 (for 사용)

def my_sum(n):
    result = 0
    for num in range(1, n+1):
        result += num
    return result

answer = my_sum(10)
print(answer)

# 5. 4번을 while로 바꿔보세요

def my_sum(n):
    i = 0
    result = 0
    while i > n:
        result + [i]
        i += 1
    return result

#solution
def my_sum(n):
    result = 0
    while n != 0:
        result += n
        n -= 1
    return result

# 6. 주어진 리스트에서 가장 큰 값을 찾아주는 함수를 작성해 보세요.

# 7. 재귀 함수로 바꿔보세요.

def recur(n):
    print(n)
    if n == 10:
        return n
    else:
    recur(n+1)


result = recur(0)
print(result)

def my_sum(n):
    if n == 0:
        return 0
    return n + my_sum(n - 1)
my_sum(10)