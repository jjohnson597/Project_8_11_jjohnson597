"""
Program: RPG Adventure Simulator 2 - Save Manager Tests
Author: Jaylen Johnson
Purpose: Provides automated unit tests for the save manager functionality.
Starter code: Original tests created for this project using unittest.
Date: 7/19/2026
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from character import Player
from save_manager import load_game, save_game


class TestSaveManager(unittest.TestCase):

    def setUp(self):
        """Create a temporary save location before each test."""
        self.temp_directory = tempfile.TemporaryDirectory()
        self.temp_save_file = Path(self.temp_directory.name) / "save_file.json"

    def tearDown(self):
        """Remove the temporary files after each test."""
        self.temp_directory.cleanup()

    def test_save_game_creates_json_file(self):
        """Saving should create a JSON file containing player data."""
        player = Player("Jaylen")
        player.level = 3
        player.gold = 25

        with patch("save_manager.SAVE_FILE", self.temp_save_file):
            save_game(player)

        self.assertTrue(self.temp_save_file.exists())

        with self.temp_save_file.open("r", encoding="utf-8") as file:
            saved_data = json.load(file)

        self.assertEqual(saved_data["name"], "Jaylen")
        self.assertEqual(saved_data["level"], 3)
        self.assertEqual(saved_data["gold"], 25)

    def test_load_game_restores_player(self):
        """Loading should restore saved player attributes."""
        saved_data = {
            "name": "Jaylen",
            "level": 4,
            "health": 20,
            "max_health": 36,
            "attack": 9,
            "gold": 42,
            "inventory": ["Iron Sword", "Health Potion"]
        }

        with self.temp_save_file.open("w", encoding="utf-8") as file:
            json.dump(saved_data, file)

        with patch("save_manager.SAVE_FILE", self.temp_save_file):
            loaded_player = load_game()

        self.assertIsNotNone(loaded_player)
        self.assertEqual(loaded_player.name, "Jaylen")
        self.assertEqual(loaded_player.level, 4)
        self.assertEqual(loaded_player.health, 20)
        self.assertEqual(loaded_player.max_health, 36)
        self.assertEqual(loaded_player.attack, 9)
        self.assertEqual(loaded_player.gold, 42)
        self.assertEqual(
            loaded_player.inventory,
            ["Iron Sword", "Health Potion"]
        )

    def test_load_game_missing_file_returns_none(self):
        """Loading a missing file should return None."""
        with patch("save_manager.SAVE_FILE", self.temp_save_file):
            loaded_player = load_game()

        self.assertIsNone(loaded_player)

    def test_load_game_invalid_json_returns_none(self):
        """Loading invalid JSON should return None."""
        self.temp_save_file.write_text(
            "This is not valid JSON",
            encoding="utf-8"
        )

        with patch("save_manager.SAVE_FILE", self.temp_save_file):
            loaded_player = load_game()

        self.assertIsNone(loaded_player)


if __name__ == "__main__":
    unittest.main()