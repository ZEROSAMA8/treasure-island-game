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
Firoad= print(input("You're at a cross road. whare do you want to go? Type 'left' or 'right'\n "))
firoadl= Firoad.lower()
if firoadl == "left":
  secroad=input("You came to a lake. There is an Island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across." )
  print(secroad)                     
secroadl = secroad.lower()
  if secroadl == "wait":
    wait= print(input("You arrive at the Island unharmed. There is a house with 3 doors, one red, one yellow and one blue. Whitch coluor do you choose?\n "))
    waitl= wait.lower() 
    if waitl == "yello":
       print("(((((: Congratulations you have won this game((((((:")
    elif waitl == "red":
      print("You got Burned by the fire. Game over.")
    elif waitl =="blue":
        print("Yuou got Eaten by beats, Game over.")
    else:
        print("Game over")
  else:
  print("You got Attacked by trout. Game over")
else:
print("You have Fall into a hole, You are screwed Game Over.")

print("Would you like to play again?")
