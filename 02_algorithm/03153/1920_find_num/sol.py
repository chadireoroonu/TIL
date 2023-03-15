import sys
sys.stdin = open('input.txt')

# 시간초과 오답
# 문자열로 저장하여 in 비교 시, 두 자리 이상의 수를 분리하여 출력오류 발생
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
m = int(sys.stdin.readline())
target = sys.stdin.readline().split()

for i in target:
    if i in arr:
        print(1)
    else:
        print(0)