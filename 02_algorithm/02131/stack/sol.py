# 스택 클래스 만들기
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.top = -1

    # 값이 비었는지 확인하는 메서드
    # 스택이 비었는지는 top으로 확인 가능
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    # 값을 추가하는 메서드
    def push(self, item):
        # 가득차지 않았을 때만 추가
        is self()
        self.top += 1
        self.items[self.top] = item

    # 현재 top 위치에 있는 값 출력
    def peek(self):
        if self.is_empty():
            return Exception('스택이 비었다.')
        return self.items[self.top]

    # 가득 찼는지 확인하는 메서드
    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return  False

    # 값을 제거
    def pop(self):
        if self.is_empty():
            pass
        else:
            value = self.items[self.top]
            self.top -= 1
            return value

# 길이가 5인 스택 생성하기
s1 = Stack(5)
print(s1.items)
print(s1.top)
print(s1.is_empty())
#s1에 값 a를 추가
s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')
s1.push('e')
print(s1.items)
print(s1.top)
print(s1.peek())
s2 = Stack(5)
print(s2.peek()) # 스택이 비었다는 사실을 알려야함