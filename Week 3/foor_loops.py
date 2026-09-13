# Uncomment each chunk of code below to run it and remind yourself of the concepts taught in class

# For loops

# Simple for loop
# fruit_list = ["oranges", "apples", "strawberries", "blueberries"]
# for fruit in fruit_list:  # for and in are keywords. You can use any word instead of fruit as long as you use the same word inside the for loop to refer to the item in the list.
#     print("I like ", fruit)

# For Loop within a For loop
# vegetable_list = ["broccoli", "carrot", "celery"]
# groceries = [fruit_list, vegetable_list]
# for list in groceries:
#     for item in list:
#         print("I like ", item)

#print(groceries[1][:2]) #to access specific item 
# for list in groceries: #to access specific items
#     print(list[:2])

# For loop using range function
# for y in range(3):  # range(3) starts at 0 and goes to 2 in steps of 1 (0,1,2)
#     print("You should buy: ", fruit_list[y])
# Break in For loop
# for vegetable in vegetable_list:
#     print(vegetable)
#     if (vegetable == "carrot"):
#         break
