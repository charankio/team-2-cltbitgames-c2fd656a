from unittest import TestCase
from levelup.map import GameMap


class TestGetPosition(TestCase):
    def test_calculatePosition(self):
        testObj = GameMap.calculatePosition([1, "b"], "F")
        self.assertEqual(testObj, [1, "b"])

    def test_isPositionValid(self):
        testObj = GameMap.isPositionValid([3, "f"])
        assert testObj == False
