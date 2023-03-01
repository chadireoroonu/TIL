n = int(input())

queue = [0, 1]
i = 0
while i <= n-2:
    num = queue.pop(0) + queue[0]
    queue.append(num)
    i += 1

print(queue[-1])