sen = input() + ' '

word = ''
words = []
for i in sen:
    if i != ' ':
        word += i
    else:
        words.append(word)
        word = ''

counting = 0
for i in words:
    counting += 1

print(counting)