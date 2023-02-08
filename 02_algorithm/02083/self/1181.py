import sys
sys.stdin = open('input.txt')

n = int(input())
words = []
for tc in range(n):
    w = input()
    if w not in words:
        words.append(w)

result = []
for j in range(len(words)):
    mini = words[0]
    for i in words:
        if len(i) < len(mini):
            mini = i
        elif len(i) == len(mini):
            if i < mini:
                mini = i

    result.append(mini)
    words.remove(mini)

for i in result:
    print(i)