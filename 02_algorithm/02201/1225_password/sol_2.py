import sys
sys.stdin = open('input.txt')

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]


for case in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    cQ_size = 8
    cQ = password
    front = rear = 0

    for i in range(8):

