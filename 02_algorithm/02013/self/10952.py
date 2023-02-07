while True:
    a, b = list(map(int, input().split()))
    if a != 0:
        print(a+b)
    else:
        if b != 0:
            print(a+b)
        else:
            break

