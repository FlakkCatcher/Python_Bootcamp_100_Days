# UNDERSTANDING THE OFFSET AND APPENDING ITEMS TO LISTS

# Normally, when we have a variable name, it is assigned a single value

# With lists, you can store a whole chunk of related data together as one item

# Example List
fruits = ["apple", "pear", "banana"]
print(fruits)
#
# # To add something into the list, use the LIST.append function

fruits.append("pineapple")
print(fruits)

# The list takes the place of many different variables
# Counting in a list starts with 0 because the first item is 0 spaces away from the start of the list
# The second item in the list has the index of 1 because it is 1 item away from the start of the list and so on

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

order = int(input("Select a number to find the order in which it joined the Union: "))-1
# When the user enters 1, we actually want to call the item indexed at 0, so their input needs a -1 at the end
print()
print(f"The state that joined in that order is: {states_of_america[order]}.")

# You can also count through the list backwards using negative indexes starting at -1, then -2, and so on
reverse = int(input("Or you can list the states  backward starting with Hawaii as #1: "))*-1
print()
print(f"The state that joined {reverse*-1} from the end is: {states_of_america[reverse]}.")

# You can also change the values within the list one at a time by directing calling that index
fruits2 = ["apple", "pear", "banana"]
fruits2[2] = "banananananananananananana"
print(fruits2)

fruits2.append("Taters")
print(fruits2)

fruits2.extend(["tomatoes....ewww", "star fruit", "jackfruit"])
print(fruits2)