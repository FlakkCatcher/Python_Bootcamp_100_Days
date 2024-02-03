# MULTIPLE IF STATEMENTS

# Using multiple if-statements can check for multiple conditions, each with their own if-then

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif 12 < age < 18:
        bill = 7
        print("Youth tickets are $7.")
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
