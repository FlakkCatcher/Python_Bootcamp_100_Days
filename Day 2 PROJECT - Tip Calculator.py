# If the bill was $150.00, split between 5 people, with a 12% tip.

# Each person should pay (150.00/5)*1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number.  You might have to do some Googling to solve this.

# Write your code below this line.

print("Welcome to the tip calculator!")
print("------------------------------\n")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percent tip would you like to give?\n"))
people = int(input("How many people are you splitting this by?\n"))
print()
tip_total = bill*(tip/100)
total_bill = bill+tip_total
per_person = round(total_bill/people, 2)
print(f"Each person should pay: ${per_person}.")
