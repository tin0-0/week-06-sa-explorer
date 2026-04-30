players = ["Scrumhalf-Faf de Klerk", "Flyhalf-Handré Pollard", "Lock-Etzebeth", "Lock-Marcell Coetzee", "Flanker-Siya Kolisi", "Flanker-Allister Highton"]
print("The Springbok Rugby Team:")
for i, player in enumerate(players, start=1):
    print(f"{i}. {player}")
while True:
    if input("Would you like to add or remove a player(yes/no)").lower()=="yes":
        ask = input("type 'add' to add a player or 'remove' to remove a player:")
        if ask.lower() == "add":
            new_player = input("Enter the name and position of the new player (e.g., 'Position-Name'):")
            players.append(new_player)
            print(f"{new_player} has been added to the team.")
        elif ask.lower() == "remove":
            player_to_remove = input("Enter the name and position of the player to remove (e.g., 'Position-Name'):")
            if player_to_remove in players:
                players.remove(player_to_remove)
                print(f"{player_to_remove} has been removed from the team.")
            else:
                print(f"{player_to_remove} is not on the team.")
    else:
        break
print("Updated Springbok Rugby Team:")
for i, player in enumerate(players, start=1):
    print(f"{i}. {player}")        


    