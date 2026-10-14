n = 5

i = 1
while i < n:
    for j in range(i):     # runs i times: 1, 2, 4, 8, ...
        total += 1         # O(1)
    i = i * 2              # i doubles: 1, 2, 4, 8, ...

    