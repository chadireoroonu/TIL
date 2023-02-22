import sys
sys.stdin = open('input.txt')

# 스위치의 숫자와 스위치 on, off 여부 저장 
t = int(sys.stdin.readline())
swich = list(map(int, sys.stdin.readline().split()))

# 주어지는 n 만큼 성별과 숫자 입력 
n = int(sys.stdin.readline())
for q in range(n):
    g, m = list(map(int, sys.stdin.readline().split()))
    
    # 성별이 남자라면, 스위치의 전 번호(1~n)을 순회하며 
    # i+1이 m의 배수인 경우에 스위치의 정보 반대로 변환 
    if g == 1:
        for i in range(t):
            if (i+1) % m == 0:
                if swich[i] == 1:
                    swich[i] = 0
                else:
                    swich[i] = 1
    # 성별이 여자라면, 임시 리스트를 생성하고
    # 번호 -1(스위치 번호와 맞추기 위해) 리스트에 추가 
    temp = []
    if g == 2:
        temp.append(m-1)
        
        # while 반복하는 동안 증가할 임시 변수 선언
        # 만약 m-u, m+u가 스위치 리스트 안에 있고
        # (스위치의 숫자 범위 때문에 부등호 조정) 
        # 스위치의 m-u-1, m+u-1이 동일한 값을 가지면
        # 임시리스트 temp에 해당 인덱스 추가
        # 같지 않거나 범위를 벗어난다면 반복문 종료 
        u = 1
        while True:
            if 0 < m-u <= t and 0 < m+u <= t and swich[m-u-1] == swich[m+u-1]:
                temp.append(m-u-1)
                temp.append(m+u-1)
                u += 1
            else:
                break
    
    # 인덱스를 저장한 리스트를 순회하며
    # 스위치 정보를 반대로 변환 
    for j in temp:
        if swich[j] == 1:
            swich[j] = 0
        else:
            swich[j] = 1

# 스위치 리스트의 요소들을 20개씩 빈칸을 두고 출력
for i in range(0, t, 20):
    print(*swich[i:i+20])