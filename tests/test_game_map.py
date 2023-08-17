from unittest import TestCase
from levelup.map import GameMap


class TestGetPosition(TestCase):
    def test_calculatePosition(self):
        testObj = GameMap.calculatePosition([1, "b"], "F")
        self.assertEqual(testObj, [1, "b"])