def check(nums, quick):
    if quick:
        return nums[0]        # O(1)
    else:
        total = 0
        for x in nums:        # O(n)
            total += x
        return total

    