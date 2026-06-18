"""
Program: Video Game collection manager
Author: Abass Hassan
Purpose: A simple program to manage your game.
Resources: Course Chapters 1-7
Date: June 2026
"""

player_name = input("Enter your name: ")
print(f"Welcome, {player_name}")

games = {
    "Scarlet Hollow": 9,
    "Pathfinder Wotr": 10,
    "Hades": 8
}
#Number is game rating out of 10

while True:
    print("\n=== Video Game Collection Manager ===")
    print("1. View Games")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Search Game")
    print("5. Exit")

    choice = input("Choose an option: ")

if choice == "1":
    print("\nGame Collection:")
    for game, rating in games.items():
        print(f"{game} - Rating: {rating}/10")
elif choice == "2":
    game = input("Enter game title: ")
    rating = int(input("Enter rating (1-10): "))
    games[game] = rating
    print("Game added")
elif choice == "3":
    game = input("Enter game to remove: ")
    if game in games:
        del games[game]
        print("Game removed")
    else:
        print("Game not found")