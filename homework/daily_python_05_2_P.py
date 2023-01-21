import calc

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("'0'으로는 나눌 수 없습니다.")

print(calc.add(2, 3)) # 5
print(calc.sub(2, 3)) # -1
print(calc.mul(2, 3)) # 6
print(calc.div(2, 3)) # 0.6666666666666666

print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.