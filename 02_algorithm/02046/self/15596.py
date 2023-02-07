def solve(a):
    ans = 0
    for i in a:
        if type(i) == int:
            ans += i

    return ans

b = [1, 'f', 3, 4, 5, 6, 'd', 'a']

print(solve(b))
print(1+3+4+5+6)