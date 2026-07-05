"""
Program: RPG Adventure Simulator 2 - Game Data
Author: Jaylen Johnson
Purpose: Stores reusable game data for locations, enemies, and shop items.
Starter code: Adapted from my Project 1 RPG Adventure Simulator.
Date: 7/12/2026
"""

import random

from character import Player
from game_data import LOCATIONS, ENEMIES, SHOP_ITEMS

def view_character(player):
    """Display the player's current character statistics."""
    print("\nCharacter Stats")
    print("---------------")
    print(f"Name: {player.name}")
    print(f"Level: {player.level}")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Attack: {player.attack}")
    print(f"Gold: {player.gold}")
    input("\nPress Enter to continue...")

def view_inventory(player):
    """Display all items currently in the player's inventory."""
    print("\nInventory")
    print("---------")

    for item in player.inventory:
        print(f"- {item}")

    input("\nPress Enter to continue...")

def use_health_potion(player, inventory):
    """Use a health potion from inventory to restore player health."""
    if "Health Potion" in inventory:
        inventory.remove("Health Potion")

        heal_amount = 15
        player["health"] += heal_amount

        if player["health"] > player["max_health"]:
            player["health"] = player["max_health"]

        print("\nYou drink a Health Potion.")
        print(f"You recovered {heal_amount} health.")
        print(f"Current Health: {player['health']}/{player['max_health']}")
    else:
        print("\nYou don't have a Health Potion!")

    input("\nPress Enter to continue...")

def rest(player):
    """Restore the player's health to the maximum value."""
    player["health"] = player["max_health"]

    print("\nYou rest at camp and recover your health.")
    print(f"Health restored to {player['health']}/{player['max_health']}.")

    input("\nPress Enter to continue...")

def visit_shop(player, inventory, shop_items):
    """Allow the player to purchase items from the shop."""
    print("\nShop")
    print("----")
    print(f"Your Gold: {player['gold']}")

    for item, price in shop_items.items():
        print(f"{item}: {price} gold")

    item_choice = input("\nEnter the item name to buy or type 'exit': ")

    if item_choice == "exit":
        print("\nYou leave the shop.")

    elif item_choice in shop_items:
        item_price = shop_items[item_choice]

        if player["gold"] >= item_price:
            player["gold"] -= item_price
            inventory.append(item_choice)

            print(f"\nYou bought {item_choice}!")

            if item_choice == "Iron Sword":
                player["attack"] += 3
                print("Your attack increased by 3.")

            elif item_choice == "Steel Shield":
                player["max_health"] += 5
                player["health"] += 5
                print("Your max health increased by 5.")

        else:
            print("\nYou do not have enough gold.")

    else:
        print("\nThat item is not sold here.")

def challenge_boss(player):
    """Allow the player to challenge the final boss if they meet the level requirement."""
    if player["level"] >= 3:
        print("\nYou challenge the Dragon King...")
        print("After a difficult battle, you defeat the Dragon King!")
        print("You win the game!")
        return True

    print("\nYou are not strong enough yet.")
    print("Reach level 3 before challenging the Dragon King.")
    input("\nPress Enter to continue...")
    return False

def explore(player, inventory, locations, monsters):
    """Allow the player to explore a random location and experience a random event."""
    location = random.choice(locations)
    event = random.choice(["gold", "item", "monster", "nothing"])

    print(f"\nYou explore the {location}.")

    if event == "gold":
        found_gold = random.randint(3, 10)
        player["gold"] += found_gold
        print(f"You found {found_gold} gold!")

    elif event == "item":
        found_item = random.choice(["Old Shield", "Magic Herb", "Iron Dagger"])
        inventory.append(found_item)
        print(f"You found a {found_item}!")

    elif event == "monster":
        monster = random.choice(monsters)
        monster_health = monster["health"]

        print(f"\nA wild {monster['name']} appears!")

        while monster_health > 0 and player["health"] > 0:
            print(f"\nYour Health: {player['health']}")
            print(f"{monster['name']} Health: {monster_health}")

            input("Press Enter to attack...")

            monster_health -= player["attack"]
            print(f"You hit the {monster['name']}!")

            if monster_health <= 0:
                break

            player["health"] -= monster["attack"]
            print(f"The {monster['name']} attacks you!")

        if player["health"] > 0:
            print(f"\nYou defeated the {monster['name']}!")
            player["gold"] += monster["gold"]
            player["level"] += 1
            player["attack"] += 1
            player["max_health"] += 2
            player["health"] = player["max_health"]

            print(f"You earned {monster['gold']} gold!")
            print("You leveled up!")
            print(f"Level: {player['level']}")
            print(f"Attack increased to {player['attack']}.")
            print(f"Max health increased to {player['max_health']}.")

        else:
            print("\nYou were defeated...")
            player["health"] = player["max_health"]
            print("You wake up safely back at camp.")

    else:
        print("You did not find anything this time.")

    input("\nPress Enter to continue...")

print("Welcome to RPG Adventure Simulator!")
print("Create your hero and begin your journey.")

player = Player(player_name)
print(f"\nWelcome, {player['name']}!")

locations = ("Forest", "Cave", "Abandoned Road")

monsters = [
    {"name": "Goblin", "health": 10, "attack": 3, "gold": 5},
    {"name": "Skeleton", "health": 15, "attack": 4, "gold": 8},
    {"name": "Orc", "health": 20, "attack": 5, "gold": 12}
]

boss_defeated = False

shop_items = {
    "Health Potion": 8,
    "Iron Sword": 20,
    "Steel Shield": 15
}

while True:
    print("\n==========================")
    print(" RPG Adventure Simulator")
    print("==========================")
    print("1. View Character")
    print("2. Explore")
    print("3. View Inventory")
    print("4. Use Health Potion")
    print("5. Rest")
    print("6. Visit Shop")
    print("7. Challenge Dragon King")
    print("8. Quit")

    choice = input("\nChoose an option (1-8): ")

    if choice == "1":
        view_character(player)

    elif choice == "2":
        explore(player, inventory, locations, monsters)

    elif choice == "3":
        view_inventory(player)

    elif choice == "4":
        use_health_potion(player, inventory)

    elif choice == "5":
        rest(player)

    elif choice == "6":
        visit_shop(player, inventory, shop_items)

    elif choice == "7":
        boss_defeated = challenge_boss(player)

        if boss_defeated:
            break

    elif choice == "8":
        print("\nThanks for playing. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")
        input("\nPress Enter to continue...")

    