def summarize(nums):
    total = 0                 # O(1)
    for x in nums:            # O(n): runs once per item
        total += x
    print(total)              # O(1)
    return total              # O(1)

