import sys
sys.stdin = open('input.txt')

a = int(input())
b = int(input())
c = int(input())

result = {'0':0, '1':0, '2':0, '3':0, '4':0,
          '5':0, '6':0, '7':0, '8':0, '9':0}

n = str(a * b * c)

for i in n:
    result[i] += 1

for i in result:
    print(result[i])
