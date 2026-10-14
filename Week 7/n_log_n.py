n=5

i = 1
while i < n:
    for j in range(n):     # runs n times on every pass
        total += 1         # O(1)
    i = i * 2              # i doubles: 1, 2, 4, 8, ...

    