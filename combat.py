player = {
    "name": "Isaac",
    "attack": 10,
    "heal": 15,
    "health": 100
}

monster = {
    "name": "monster",
    "attack": 50,
    "health": 100
}

print("""
A wild monster attacks!
Choose an action!
.
.
.
1. Attack
2. Heal
- - - - - - - - - - - - - - -""")

game_running = True
while game_running == True:

    print("Your action: ", end="")
    player_choice = input()

    if player_choice == "1":
        print("Attacking monster!")
        print("")
        player["health"] = player["health"] - monster["attack"]
        monster["health"] = monster["health"] - player["attack"]
        print("Player's health: " + str(player["health"]))
        print("Monster's health: " + str(monster["health"]))
        print("- - - - - - - - - - - - - - -")
    elif player_choice == "2":
        print("Healing player!")
        print("")
        player["health"] = player["health"] + player["heal"] - monster["attack"]
        print("Player's health: " + str(player["health"]))
        print("Monster's health: " + str(monster["health"]))
        print("- - - - - - - - - - - - - - -")
    else:
        print("Choose a valid action!")

    if player["health"] <= 0:
        print("You lose!")
        break
    elif monster["health"] <= 0:
        print("You win!")
        break
    else:
        continue