# NUMBER MANIPULATION AND F-STRINGS

# All division results in a float which has an infinite set of numbers after the decimal
print(8/3)
print("-----")

# We can select only the first number by converting it into an integer
print(int(8/3))
print("-----")

# Or we can use the round function which rounds to the number of places you specifiy
print(round(8/3))       # Rounds to the nearest whole number
print(round(8/3, 1))    # Rounds to 1 digit after the decimal
print(round(8/3, 2))    # Rounds to 2 digits after the decimal and so on
print("-----")

# The floor division number gives you just the absolute number of times something can be divided
# This type of division is automatically an integer
print(8//3)
print("-----")

# Saving math operations as a variable means you can continue to use the variable as the original equation
result = 4/2
print(result/2)
print("-----")

# Using variables also allows for the recursive math operations (+=, -=, /=, *=, **=)
result += 1     # Adds one to the previous value for result
print(result)
print("-----")

# F-Strings allow for mixing different data types
print("Your score is " + str(result) + ".")       # Before, we had to convert the variable into a string
print(f"Your score is {result}.")
score = 0
height = 1.0
isWinning = True
print(f"Your score is {score}, your height is {height}m, and you are winning is {isWinning}.")
