import unittest
from .solution import peak_height


class TestBirdMountain(unittest.TestCase):
    def test_empty(self):
        mountain = [
            "      ",
            "      ",
            "      "
        ]
        self.assertEqual(peak_height(mountain), 0)

    def test_stone(self):
        mountain = [
            "              ",
            "              ",
            "              ",
            "              ",
            "     ^        "
        ]
        self.assertEqual(peak_height(mountain), 1)

    def test_simple_mountain(self):
        mountain = [
            "^^^^^^        ",
            " ^^^^^^^^     ",
            "  ^^^^^^^     ",
            "  ^^^^^       ",
            "  ^^^^^^^^^^^ ",
            "  ^^^^^^      ",
            "  ^^^^        "
        ]
        self.assertEqual(peak_height(mountain), 3)

    def test_twice(self):
        mountain = [
            "^^^^^^        ",
            " ^^^^^        ",
            "              ",
            "  ^^^^^^  ^^  ",
            "  ^^^ ^^^^  ^ ",
            "  ^^^^^^      ",
            "  ^^^^     ^  "
        ]
        self.assertEqual(peak_height(mountain), 2)

    def test_vulcano(self):
        mountain = [
            "          ^^^^^^^^^          ",
            "        ^^^^^^^^^^^^^        ",
            "      ^^^^^^^^^^^^^^^^^      ",
            "     ^^^^^^^     ^^^^^^^     ",
            "    ^^^^^^^       ^^^^^^^    ",
            "    ^^^^^^^       ^^^^^^^    ",
            "    ^^^^^^^       ^^^^^^^    ",
            "     ^^^^^^^     ^^^^^^^     ",
            "      ^^^^^^^^^^^^^^^^^      ",
            "        ^^^^^^^^^^^^^        ",
            "          ^^^^^^^^^          "
        ]
        self.assertEqual(peak_height(mountain), 4)

    def test_plateau(self):
        mountain = [
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^",
           "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^"
        ]
        self.assertEqual(peak_height(mountain), 1)
