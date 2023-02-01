m, n = list(map(int, input().split()))

if n == 45:
    print(f'{m} 0')
elif n > 45:
    print(f'{m} {n-45}')
else:
    if m >= 1:
        print(f'{m-1} {n+15}')
    else:
        print(f'23 {n+15}')