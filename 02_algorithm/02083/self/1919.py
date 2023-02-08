import sys
sys.stdin = open('input.txt')

s1 = input()
s2 = input()

counting = 0
for i in s1:
    if i in s2:
        s2 = s2.replace(i, '', 1)
    else:
        counting += 1

print(counting+len(s2))