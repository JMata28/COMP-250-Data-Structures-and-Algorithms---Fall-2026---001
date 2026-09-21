#Notice in the code below: How does the amount of work change as the list gets larger?

numbers = [4, 8, 2, 10, 5]

largest = numbers[0] #does the speed of this line depend on the size of the list?

for number in numbers:
    if number > largest:
        largest = number

print(largest)