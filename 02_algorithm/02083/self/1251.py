n = input()

word = []
for q in range(3):
    mini = n[0]
    idx = 0
    for i in range(len(n)):
        if n[i] < mini:
            mini = n[i]
            idx = i
    word.append(n[:idx+1])
    n = n[idx+1:]

result = ''
for j in word:
    result += j[::-1]

print(result)
