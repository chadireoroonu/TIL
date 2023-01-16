t = int(input())

def m(num, a):
    {num} = list(map(int, input().split(' ')))
    return({num}, max(a))

n = 0
while t > n:
    print(m)
    n += 1