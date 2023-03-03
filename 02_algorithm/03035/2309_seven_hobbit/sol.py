import sys
sys.stdin = open('input.txt')

num = [int(input()) for _ in range(9)]

target = sum(num)

temp1 = 0    # 삭제할 난쟁이 정보 저장
temp2 = 0
for i in range(9):
    for j in range(9):
        if i != j:    # 난쟁이 키 두 명일 직접 빼기
            if target - num[i] - num[j] == 100:
                temp1 = num[i]
                temp2 = num[j]

num.remove(temp1)
num.remove(temp2)
num = sorted(num)

for i in num:
    print(i)