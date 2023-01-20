# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    result = n
    while n != 0:
        result += n % 10 # 4, 3, 2, 1
        n = n // 10
    return result

print(fn_d(91))

def is_selfnumber(m):
    # m의 제너레이터가 될 수 있는 경우는
    # 1부터 m까지의 숫자 중에 있다
    for i in range(1, m):
        # 제네레이터인지 아닌지 판별하는 방법은
        # 숫자 i를 fn_d에 집어 넣었을 때,
        # 그 값이 내가 할당받은 m과 동일하다면
        # i를 m의 제네레이터라고 할 수 있다.
        if fn_d(i) == m:
            # 하나라도 제네레이터가 있으면 셀프넘버가 아니므로
            # is_selfnumber 함수는 False를 반환하고 종료
            return False
            # else:
            #   return True가 여기가 아닌 이유는
            # 반복문 안에서 true인 상황에서 리턴하고 함수가 종료되기 때문

    # 모든 후보군을 출력했는데 False가 반환되지 않았다면
    # 셀프넘버에 해당한다.    
    return True

print(is_selfnumber(101)) # False
print(is_selfnumber(31)) # True


def is_selnumber(m):
    for i in range(1, m):
        # lambda [parameter] : expression
        # 모든 자리수의 합 + 본인 값
        # while 나머지를 사용해서 더해왔는데
        # 문자열로 바꿔서 각 자리수를 순회하며 더하기
        # '1234' -> '1', '2', '3', '4'
        # [int(char) for char in 'm'] => [1, 2, 3, 4] + [m]
        # => sum([1, 2, 3, 4, m])
        fn_d = lambda n: sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == m:
            return False
    return True


# recur.py 사용해서 while문 재귀함수 형식으로 만들어보기