"""
Program: RPG Adventure Simulator 2 - Game Data
Author: Jaylen Johnson
Purpose: Stores reusable game data for locations, enemies, and shop items.
Starter code: Adapted from my Project 1 RPG Adventure Simulator.
Date: 7/12/2026
"""

from character import Enemy


LOCATIONS = ("Forest", "Cave", "Abandoned Road")

ENEMIES = [
    Enemy("Goblin", 10, 3, 5),
    Enemy("Skeleton", 15, 4, 8),
    Enemy("Orc", 20, 5, 12)
]

SHOP_ITEMS = {
    "Health Potion": 8,
    "Iron Sword": 20,
    "Steel Shield": 15
}