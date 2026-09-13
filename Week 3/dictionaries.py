# Uncomment each chunk of code below to run it and remind yourself of the concepts taught in class

# Dictionaries
my_dictionary = {
    "Jane" : 25, 
    "Austin" : 27,
    "George" : 20
}
print("Jane's age is: ", my_dictionary["Jane"])
print("George's age is: ", my_dictionary.get("George"))
print(my_dictionary.keys())
print(my_dictionary.values())
my_dictionary["Jane"] = 30
print("Jane's age is: ", my_dictionary["Jane"])

my_dictionary["John"] = 40

if "John" in my_dictionary:
    print("You found John!")