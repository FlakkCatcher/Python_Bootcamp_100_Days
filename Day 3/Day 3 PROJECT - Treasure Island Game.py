print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print()
print("You're at a crossroads.  The way in front is blocked, so you can only go left or right.")
first = input("Which direction do you choose?  Type: 'left' or 'right'.")
if first == "left":
    print()
    print("The left-hand path leads you to a lake.  There is an island in the middle of the lake.")
    second = input("You can either swim to the island or wait for the ferry to return.  Type: 'wait' or 'swim'.")
    if second == "wait":
        print()
        print("You arrive at the island unharmed.  You find a house with three doors: red, yellow, and blue.")
        third = input("Which door do you choose? Type: 'red', 'yellow', or 'blue'.")
        if third == "yellow":
            print()
            print("You've found the treasure chest!  You win!")
        elif third == "red":
            print()
            print("The second you open the red door, flames rush out and envelop you.  You died.")
        elif third == "blue":
            print()
            print("A vicious pack of Vorpal Rabbits swarms out and devours you.  You died.")
        else:
            print()
            print("You don't know how to open a door, so you hit your head on the bricks really hard.  You died.")
    elif second == "swim":
        print()
        print("A nasty man-eating trout attacks you and swallows you whole.  You died.")
    else:
        print()
        print("While thinking of what to do, you pass out from hunger.  You died.")
elif first == "right":
    print()
    print("The right-hand path winds around a blind corner and you fall down a deep hole.  You died.")
else:
    print()
    print("You strayed off the known path and a gang of robbers find you.  You died.")
