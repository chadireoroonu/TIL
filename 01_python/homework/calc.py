# calc

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