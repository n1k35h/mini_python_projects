# Below image from https://ascii.co.uk/art
print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (o) `-.o `"=.`_.--"_o.-; ;___|___________________
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

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if choice1 == "left": # Continue the game
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
          'Type "wait" to wait for the boat or type "swim" to swim across\n').lower()
    if choice2 == "wait": # Continue the game
        choice3 = input("You have arrived to the island unharmed. "
                        "There is a house with 3 doors. A Red door, a Yellow door and a Blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It\'s a room full of fire. GAME OVER!!!") # Ends the game with a defeat
        elif choice3 == "yellow":
            print("You\'ve found a room full of Treasure. YOU HAVE WON!!!") # Ends the game with the victory
        elif choice3 == "blue":
            print("It\'s a room full a poisonous SNAKES!!! GAME OVER!!!") # Ends the game with a defeat
        else:
            print("You picked a door that doesn't exist. GAME OVER!!!") # Ends the game with a defeat
    else:
        print("You have been attacked by an angry troll! GAME OVER!!!") # Ends the game with a defeat
else:
    print("You fell into a hole. GAME OVER!!!") # Ends the game with a defeat

