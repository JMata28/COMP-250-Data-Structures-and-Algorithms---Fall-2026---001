# Uncomment each chunk of code below to run it and remind yourself of the concepts taught in class

# If, else, elif statements:
# home_team = 28
# visiting_team = 24
# if (home_team > visiting_team): #First comparison
#     print("Home team wins!")
# elif(visiting_team > home_team): #Second comparison, will only happen if first comparison returns False
#     print("Visiting team wins!")
# else:
#     print("It's a draw!")   #Default case that happens if neither first and second comparisons return True

#If-else-elif statements within other if-else-elif statements:
#The following code helps us identify which of these animals we are talking about, using if, else, and elif statements to eliminate animals:
# cat, dog, manatee, dolphin, goldfish, and frog
#Lets do this by reviewing lists and using the .remove() list method
# animal_group = "amphibian"
# has_fur = True
# feline = False
# herbivore = False
# if (animal_group == "mammal"):
#     if (has_fur == True):
#         if (feline == True):
#             animal ="cat"
#         else:
#             animal ="dog"
#     elif (herbivore ==True):
#         animal = "manatee"
#     else:
#         animal = "dolphin"
# elif (animal_group == "fish"):
#     animal ="goldfish"
# else:
#     animal ="frog"
# print("The animal is: ", animal)