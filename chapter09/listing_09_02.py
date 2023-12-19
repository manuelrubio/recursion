def play_Alice(n):
    if n <= 2:
        print('Alice wins')
    elif n & 1:
        # Alice removes one pebble
        play_Bob(n - 1)  # Turn switches to Bob
    else:
        # Alice removes two pebbles
        play_Bob(n - 2)  # Turn switches to Bob


def play_Bob(n):
    if n == 1:
        print('Bob wins')
    else:
        # Bob removes one pebble
        play_Alice(n - 1)  # Turn switches to Alice


# Test
for n in range(1, 11):
    play_Bob(n)

print()
for n in range(1, 11):
    play_Alice(n)
