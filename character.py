"""
Program: RPG Adventure Simulator 2 - Character Classes
Author: Jaylen Johnson
Purpose: Defines character classes used by the RPG game.
Starter code: Adapted from my Project 1 RPG Adventure Simulator.
Date: 7/19/2026
"""


class Character:
    """Represent a basic game character."""

    def __init__(self, name, health, attack):
        """Initialize a character with a name, health, and attack power."""
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack

    def is_alive(self):
        """Return True if the character still has health remaining."""
        return self.health > 0

    def take_damage(self, damage):
        """Reduce the character's health by the damage amount."""
        self.health -= damage

        if self.health < 0:
            self.health = 0


class Player(Character):
    """Represent the player character."""

    def __init__(self, name):
        """Initialize the player with RPG starting stats."""
        super().__init__(name, 30, 6)
        self.level = 1
        self.gold = 10
        self.inventory = ["Health Potion", "Rusty Sword"]

    def level_up(self):
        """Increase the player's level, attack, and maximum health."""
        self.level += 1
        self.attack += 1
        self.max_health += 2
        self.health = self.max_health


class Enemy(Character):
    """Represent a basic enemy character."""

    def __init__(self, name, health, attack, gold):
        """Initialize an enemy with combat stats and a gold reward."""
        super().__init__(name, health, attack)
        self.gold = gold