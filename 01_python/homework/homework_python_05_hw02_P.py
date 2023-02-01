# fn_d(91) 
# 출력 예시 
# 101

# n = int(input())

# 문항 1
# 우선, n을 입력받아 각 자릿수 숫자와 자신을 더한 숫자를 반환하는 함수 작성
n = int(input())

def fn_d(n):
    num = [n] # 합산할 숫자들을 모을 리스트 생성, n도 더해야하므로 리스트에 추가
    while n != 0: # n을 10으로 나눈 몫이 0이 될때까지 각 몫을 n으로 설정
        n // 10
        num.append(n % 10) # 리스트에는 n을 10으로 나눈 나머지 추가
        n = n // 10
    return sum(num) # 각 리스트의 합을 구해 n과 각 자릿수 합산

# print(fn_d(n)) 
    
# 문항 2
# n의 제네레이터가 있는지 판별하는 과정
def is_selfnumber(n):
    i = 1
    generator = []
    while i < n: # i가 n보다 작은 동안 제너레이터 리스트에 fn_d(i) 추가
        generator.append(fn_d(i))
        i += 1
    if n in generator: # 만약 리스트에 n이 있다면, 셀프넘버가 아님
        return (f'{n} is not self number')
    else: # 만약 리스트에 n이 없다면, 셀프넘버에 해당함
        return (f'{n} is self number')

print(is_selfnumber(n))