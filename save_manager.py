"""
Program: RPG Adventure Simulator 2 - Save Manager
Author: Jaylen Johnson
Purpose: Saves and loads player data using a JSON file.
Starter code: Original code created for this project using Python
standard-library documentation for json and pathlib.
Date: 7/19/2026
"""

import json
from pathlib import Path

from character import Player


SAVE_DIRECTORY = Path("data")
SAVE_FILE = SAVE_DIRECTORY / "save_file.json"


def save_game(player):
    """Save the player's current progress to a JSON file."""
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)

    player_data = {
        "name": player.name,
        "level": player.level,
        "health": player.health,
        "max_health": player.max_health,
        "attack": player.attack,
        "gold": player.gold,
        "inventory": player.inventory
    }

    try:
        with SAVE_FILE.open("w", encoding="utf-8") as file:
            json.dump(player_data, file, indent=4)

        print("\nGame saved successfully.")

    except OSError as error:
        print("\nThe game could not be saved.")
        print(f"Error: {error}")

def load_game():
    """Load player progress from the JSON save file."""
    try:
        with SAVE_FILE.open("r", encoding="utf-8") as file:
            player_data = json.load(file)

        player = Player(player_data["name"])

        player.level = player_data["level"]
        player.health = player_data["health"]
        player.max_health = player_data["max_health"]
        player.attack = player_data["attack"]
        player.gold = player_data["gold"]
        player.inventory = player_data["inventory"]

        print("\nGame loaded successfully.")
        return player

    except FileNotFoundError:
        print("\nNo saved game was found.")

    except json.JSONDecodeError:
        print("\nThe save file contains invalid JSON data.")

    except KeyError as error:
        print("\nThe save file is missing required player data.")
        print(f"Missing field: {error}")

    except OSError as error:
        print("\nThe game could not be loaded.")
        print(f"Error: {error}")

    return None