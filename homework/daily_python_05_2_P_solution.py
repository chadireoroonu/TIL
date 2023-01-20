# import calc

def add(a, b):
    # 함수가 하는 가장 중요한 역할
    # code block에 작성된 특정한 로직을 '호출시마다' 실행
    # 만약 그 결과를 반환해야 한다면,
    # return 뒤에는 표현식이 올 수 있고,
    # 반드시 하나의 객체만 반환해야하는데,
    # 두 개 이상의 객체를 반환하려고 한다면 -> 튜플로 묶어서 반환
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# 단, 0으로 나눌 시, 0으로는 나눌 수 없습니다 라는 문자를 출력
def div(a, b):
    return a / b

print(div(10, 0))

try:
    print(10/0)
except ZeroDivisionError: # except 뒤에 아무것도 적지 않으면, 어떤 에러건 아래 입력한 메세지 출력
    print('0으로 나눌 수 없습니다.')
except TypeError:
    print('정수 이외의 값으로 나눌 수 없습니다.')



# print(calc.add(2, 3)) # 5
# print(calc.sub(2, 3)) # -1
# print(calc.mul(2, 3)) # 6
# print(calc.div(2, 3)) # 0.6666666666666666

# print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.

