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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_right = input('''Would you like to go left, to the river, or right and jump across a hole? (L or R): ''').lower()[0]

if left_right == 'r':
    print("You fall into the hole and die.\nThe End.")
    quit()

swim_wait = input('''\nYou arrive at the river. Would you like to wait for a boat, or swim across? W or S: ''').lower()[0]

if swim_wait == 's':
    print('''You try to swim across, but the river is deep and swift. 
You bash your head against a rock and drown.\nThe End.''')
    quit()

print('''\nA while later, a boat comes along. The pilot is willing to take you across the river.
After crossing, you thank the man, and head towards a structure in the distance.

Upon arriving, you see that it's an old ruins of a snake temple.
There are three doors, each painted a different color: Red, Blue, Yellow.''')

door = input("\nWhich door do you open? R, B, Y: ").lower()[0]

if door == 'r':
    print('''\nBehind the door is a coiled snake. It raises up and strikes you in the arm.
as the poison courses through your veins, your vision dims from the outside in.
The snake begins to swallow you, and you feel relief that the poison is acting quickly.
The End.''')
    quit()
elif door == 'b':
    print('''\nBehind the door is a beautiful priestess. She wears a flowing dress,
and around her neck, a silver snake amulet. Her eyes flash at you,
and you begin to feel your head buzzing. All of your fears abate, and you sit down.
The priestess strides over, and, looking down upon you, says, "what a fine meal for my pet." 
The blow is quick, and merciful death takes you.
The End.''')
    quit()
else:
    print('''\nThe treasure of the ancient snake cult is behind this door.
Inside the chest, you find gems, gold, jewelry, all that kind of thing.
You Win!''')
    quit()
