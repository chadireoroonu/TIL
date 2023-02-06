n = int(input())

k = 0
for i in range(8):
    if n // 3 == 1:
        k += 1
        break
    else:
        n = n // 3
        k += 1

def three(k):
    if k == 1:
        return '''
        ***
        * *
        ***
        '''
    else:
        return 3 * three(k-1)

print(three(k))