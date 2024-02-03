# LOGICAL OPERATORS

# Logical operators are the "and", "or", and "not" operations which produce Boolean values when their conditions are met

# For AND, both conditions must be true for it to be true; otherwise it's false
a = 12
print(a > 15)
print(a < 10)
print(a < 15 and a > 10)    # Both are true, so the entire statement is true
print(a < 15 and a > 13)    # The second one is false, so the entire statement is false

print("----------------")
# For OR, only one of the conditions (or both) needs to be true for the statement to be true
b = 10
print(b > 8 or b == 10)     # Both are true, so the entire statement is true
print(b > 8 or b == 9)      # The second one is false, but the first is true, so the entire statement is true
print(b > 11 or b == 9)     # Both are false, so the entire statement is false

print("----------------")
# For NOT, it just reverses the logical condition, so true becomes false and vice-versa
c = 12
print(c > 13)               # This is a false statement
print(not c > 13)           # This now becomes a true statement

print("----------------")

# This new version assumes that people aged 45-55 just need a free ticket because they just do...
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age < 18:                # Used "and" to create an age window
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:               # Used "and" to create an age window
        bill = 0
        print("Everything is going to be okay.  Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken?  Y or N. ")

    # New if-statements is placed at the same indent as the original if-statement to check a new condition
    # Since we're checking a single Y/N question, we don't actually need the companion else-statement

    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

