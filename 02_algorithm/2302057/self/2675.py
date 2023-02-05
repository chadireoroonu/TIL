t = int(input())
for i in range(t) :
    r, s = list(map(str, input().split()))

    string = []
    for i in range(len(s)):
        string.append(s[i])

    result = ''
    for i in string:
        result += i * int(r)

    print(result)