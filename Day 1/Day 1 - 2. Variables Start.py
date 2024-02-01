# VARIABLES

name = input("What is your name? ")
print(name)

# Remember, variable values can always be changed inside the code itself
# This just needs the variable to be assigned a new value at some point after it's assigned
#   the first value.

name = "Jim Bob"
print(name)

# In line 8, the value was changed to "Jim Bob" rather than whatever was input before
# Below, it gets changed again

name = input("What is your name? ")
length = len(name)
print(length)
