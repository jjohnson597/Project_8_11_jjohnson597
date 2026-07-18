"""
Program: RPG Adventure Simulator 2 - Save Manager
Author: Jaylen Johnson
Purpose: Saves and loads player data using a JSON file.
Date: 7/19/2026
"""

import json
from pathlib import Path

from character import Player


SAVE_DIRECTORY = Path("data")
SAVE_FILE = SAVE_DIRECTORY / "save_file.json"


def save_game(player):
    """Save the player's current progress to a JSON file."""
    SAVE_DIRECTORY.mkdir(exist_ok=True)

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