numbers = [4, 8, 2, 10, 5]
target = 10

for number in numbers:
    if number == target:
        print("Found!")
        break

'''
If the list contains more items, the algorithm may need to examine more items. 
Algorithm analysis helps us understand how that workload changes with the size of the input.
'''