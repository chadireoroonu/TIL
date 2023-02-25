import sys
sys.stdin = open('input.txt')

def reverse(w):
    global count
    temp = True
    for i in range(len(w) - 1):
        if word[i] != word[i + 1]:
            temp = False
    if temp == True:
        return count
    else:
        count += 1
        idx_f = 0
        idx_b = 0
        for i in range(len(w)-1):
            if w[i] != w[i+1]:
                idx_f = i + 1
                break
        for i in range(len(w)):
            if w[-i-1] != w[-i-2]:
                idx_b = -i-1
                break
        if idx_f == len(w)+idx_b:
            return count
        if w[idx_f:idx_b]:
            return reverse(w[idx_f:idx_b])
        else:
            return count

word = sys.stdin.readline()
count = 0
print(reverse(word))
