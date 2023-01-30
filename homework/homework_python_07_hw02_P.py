def collatz(num):
    counting = 0
    if num == 1:
        return print(counting)
    elif num % 2 == 0:
        counting += 1
        return collatz(num // 2)
    elif num % 2 != 0:
        counting += 1
        return collatz(num * 3 + 1)

    
collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1