import sys
sys.stdin = open('input.txt')

n, k = list(map(int, sys.stdin.readline().split()))
room = 0
female = []    # 성별 리스트 생성 후 학년별 학생 수 기록
male = []
for nc in range(n):
    s, y = list(map(int, sys.stdin.readline().split()))
    if s == 0:
        female.append(y)
    else:
        male.append(y)

gender = [female, male]
for i in range(1, 7):    # 모든 학년의 해당 성별 학생 방 배정
    for j in range(2):
        temp = gender[j].count(i)
        if temp % k:
            room += temp // k + 1
        else:
            room += temp // k

print(room)
