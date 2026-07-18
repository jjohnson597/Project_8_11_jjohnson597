"""
Program: RPG Adventure Simulator 2 - Character Tests
Author: Jaylen Johnson
Purpose: Provides automated unit tests for RPG character classes.
Starter code: Original tests created for this project using unittest.
Date: 7/19/2026
"""

import unittest

from character import Character, Player, Enemy


class TestCharacterClasses(unittest.TestCase):

    def test_player_defaults(self):
        """Player starts with the correct default values."""
        player = Player("Jaylen")

        self.assertEqual(player.name, "Jaylen")
        self.assertEqual(player.level, 1)
        self.assertEqual(player.health, 30)
        self.assertEqual(player.attack, 6)
        self.assertEqual(player.gold, 10)

    def test_player_inventory(self):
        """Player begins with the default inventory."""
        player = Player("Jaylen")

        self.assertIn("Health Potion", player.inventory)
        self.assertIn("Rusty Sword", player.inventory)

    def test_enemy_creation(self):
        """Enemy attributes should initialize correctly."""
        enemy = Enemy("Goblin", 10, 3, 5)

        self.assertEqual(enemy.name, "Goblin")
        self.assertEqual(enemy.health, 10)
        self.assertEqual(enemy.attack, 3)
        self.assertEqual(enemy.gold, 5)

    def test_take_damage(self):
        """Taking damage should reduce health."""
        player = Player("Jaylen")

        player.take_damage(10)

        self.assertEqual(player.health, 20)

    def test_level_up(self):
        """Leveling up should improve player stats."""
        player = Player("Jaylen")

        player.level_up()

        self.assertEqual(player.level, 2)
        self.assertEqual(player.attack, 7)
        self.assertEqual(player.max_health, 32)


if __name__ == "__main__":
    unittest.main()