# 1번 문제
n = int(input())

num = []
for i in range(1, n+1):
    if n % i == 0:
        num.append(i)
    else:
        pass
num.sort()

print(num)


# 2번 문제
num = eval(input())
def list_sum(num):
    sum = 0
    for i in num:
        sum += i
    return sum

print(list_sum(num))


# 3번 문제
dict = eval(input())
def dict_list_sum(dict):
    sum = 0
    for i in range(len(dict)):
        sum += dict[i]['age']
    return sum

print(dict_list_sum(dict))


# 4번 문제
num = eval(input())
def all_list_sum(num):
    sum = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            sum += num[i][j]
    return sum

print(all_list_sum(num))

ascii = {
    65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F',
    71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L',
    77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R',
    83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X',
    89: 'Y', 90: 'Z', 97: 'a', 98: 'b', 99: 'c', 100: 'd',
    101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j',
    107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 
    113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v',
    119: 'w', 120: 'x', 121: 'y', 122: 'z'
}

# 5번 문제
numbers = eval(input())
alphabet = []
def get_secret_word(numbers):
    for i in range(len(numbers)):
        alphabet.append(ascii[numbers[i]])
    word = alphabet[0]
    for j in range(1, len(alphabet)):
        word += alphabet[j]
    return word

print(get_secret_word(numbers))


# 6번 문제
ascii_reverse = dict(zip(ascii.values(),ascii.keys()))

words = input()
def get_secret_number(words):
    numbers = []
    for i in range(len(words)):
        numbers.append(ascii_reverse[words[i]])
    sum = 0
    for j in range(len(numbers)):
        sum += numbers[j]
    return sum

print(get_secret_number(words))


# 7번 문제
ascii_reverse = dict(zip(ascii.values(),ascii.keys()))

word1, word2 = input().split(',')
def get_secret_number(word1, word2):
    number1 = []
    for i in range(1, len(word1)-1):
        number1.append(ascii_reverse[word1[i]])
    sum1 = 0
    for j in range(len(number1)):
        sum1 += number1[j]

    number2 = []
    for i in range(2, len(word2)-1):
        number2.append(ascii_reverse[word2[i]])
    sum2 = 0
    for j in range(len(number2)):
        sum2 += number2[j]

    if sum1 > sum2:
        return word1
    elif sum1 == sum2:
        return word1, word2
    else:
        return word2

print(get_secret_number(word1, word2))

# 아스키 코드 교수님 힌트
# 파이썬 공식 문서에서 ord(), chr() 찾아보기!