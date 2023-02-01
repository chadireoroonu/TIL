counting = [] # 한 번 함수를 돌 때마다 1을 추가해줄 빈 리스트 생성
def collatz(num):
    while num >= 1:# 입력 숫자가 1이상일 때 작동
        if num == 1: # 만약 입력 값이 1이고
            if sum(counting) > 500: # 리스트의 합이 500 초과라면, 
                print(-1) # -1 반환
            else : # 입력 숫자가 1이고 리스트의 합이 500 이하라면,
                print(sum(counting)) # 리스트의 합 프린트 후
            return counting.clear() # 리스트를 초기화
        elif num % 2 == 0: # 만약 입력 값이 짝수라면
            counting.append(1) # 리스트에 1을 추가하고
            return collatz(num // 2) # 2로 나눈 값을 함수에 입력
        elif num % 2 != 0: # 만약 입력 값이 홀수라면
            counting.append(1) # 리스트에 1을 추가하고
            return collatz(num * 3 + 1) # 값에 3을 곱하고 1을 더해 입력값으로 넣음
    
collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1