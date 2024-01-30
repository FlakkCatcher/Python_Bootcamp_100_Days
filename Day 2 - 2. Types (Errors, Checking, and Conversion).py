# TYPE ERRORS
# The 2 lines of code below will return a TypeError because the len function creates an integer
# This integer can then not be used in a string concatenation
# num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters in it")

num_char = len(input("What is your name? \n"))
print("Your name has "+str(num_char)+" characters in it.")
# This one works because the num_char variable is turned into a string type

# TYPE CHECKING
print(type(num_char))

# TYPE CONVERSION/CASTING
num_char = len(input("What is your name? \n"))
new_num_char = str(num_char)
print("Your name has "+new_num_char+" characters in it.")
# Turned the new variable of new_num_char into a string before I put it into the final statement
print(type(num_char))
print(type(new_num_char))

print(70 + float("100.5"))  # Turns a string into a float for float addition
print(str(70)+str(100))     # Turns 2 integers into strings which then have concatenation instead of addition
