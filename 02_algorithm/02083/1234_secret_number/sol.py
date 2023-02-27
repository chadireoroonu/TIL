import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, number = list(map(int, input().split()))

    num = list(str(number))
    # print(num)

    def secret(num):
        for i in range(len(num)-1):
            while num[i] == num[i+1]:

            if num[i] == num[i+1]:
                num.remove(num[i+1])
                num.remove(num[i])
                return secret(num)
        result = ''
        for j in num:
            result += j
        return result

    print(secret(num))
