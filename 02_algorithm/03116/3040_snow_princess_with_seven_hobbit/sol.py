import sys
sys.stdin = open('input.txt')

hobbit = []
for q in range(9):
    hobbit.append(int(sys.stdin.readline().strip()))

def sol(arr):
    for i in range(9):
        for j in range(9):
            if i != j and sum(arr) - arr[i] - arr[j] == 100:
                arr.remove(arr[j])
                arr.remove(arr[i])
                return arr

sol(hobbit)

for k in hobbit:
    print(k)