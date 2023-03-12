arr = [1, 2, 3, 4, 5]

front = 0
rear = 0

target = 10

while rear < len(arr):
    if sum(arr[front:rear]) < target:
        rear += 1
    elif sum(arr[front:rear]) > target:
        front += 1
    elif sum(arr[front:rear]) == target:
        print(len(arr[front:rear]), arr[front:rear])
        rear += 1