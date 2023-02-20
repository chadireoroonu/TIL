class Queue:
    def __init__(self, n):
        self.size = n  # 전체크기
        self.items = [None] * n # 각 아이템
        self.rear = -1
        self.front = -1

    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.rear = self.rear