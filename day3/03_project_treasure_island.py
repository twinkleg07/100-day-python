print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                               
''')
print("Welcome to Treasure Island.\nYour mission is to find the tressure.\n")
print("You're at a cross road.Where do you want to go?\n")
direction = input("Type left or Right").lower()
if direction == "left" :
    wait= input("You've come to a lake. There is an island in the middle of the lake\nType 'wait' to wait for a boat. type 'swim' to swim across.").lower()
    if wait == "wait":
        door = input("You have arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?").lower()
        if door == "yellow":
            print("You found the tressure!You win\n")
        elif door =="red":
            print("It's a room full of fire. Game over!\n")
        elif door == "blue":
            print("You enter a room full of beasts. Game over!\n")
    else:
        print("You got attacked by a shark.Game over \n")
else :
    print("You fell into a hole.Game over\n")

