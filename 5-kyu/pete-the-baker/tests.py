import unittest
from .solution import cakes


class TestPeteTheBaker(unittest.TestCase):
    def test_not_enough_ingredients(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEqual(cakes(recipe, available), 0)

    def test_extra_ingredients(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(cakes(recipe, available), 2)

    def test_normal_amount_of_ingredients(self):
        recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}
        self.assertEqual(cakes(recipe, available), 11)
