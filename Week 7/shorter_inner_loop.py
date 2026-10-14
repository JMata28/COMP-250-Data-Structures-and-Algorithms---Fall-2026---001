n=5

for i in range(n):
    for j in range(i):     # runs i times, not n times
        print(i, j)        # O(1)

        